import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_tilt/flutter_tilt.dart';
import 'dart:convert';
import 'dart:io' show Platform;
import 'package:flutter/foundation.dart' show kIsWeb;

class FletTiltControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;
  const FletTiltControl({
    super.key,
    required this.parent,
    required this.control,
    required this.children,
    required this.parentDisabled,
    required this.parentAdaptive,
    required this.backend,
  });

  @override
  State<FletTiltControl> createState() => _FletTiltControlState();
}

class _FletTiltControlState extends State<FletTiltControl> {
  @override
  Widget build(BuildContext context) {
    debugPrint("FletTilt build: ${widget.control.id}");

    // Parse configurations
    TiltConfig? tiltConfig = _parseTiltConfig();
    LightConfig? lightConfig = _parseLightConfig();
    ShadowConfig? shadowConfig = _parseShadowConfig();
    ChildLayout childLayout = _parseChildLayout();

    // Parse other properties
    double? borderRadius = widget.control.attrDouble("borderRadius");
    bool disable = widget.control.attrBool("disable", false)!;
    int fps = widget.control.attrInt("fps") ?? 60;
    // LightShadowMode not available in current flutter_tilt version

    // Get child widget
    Widget? child;
    if (widget.children.isNotEmpty) {
      child = createControl(
          widget.control, widget.children.first.id, widget.control.isDisabled);
    }

    // Create Tilt widget
    Widget tiltWidget = Tilt(
      borderRadius:
          borderRadius != null ? BorderRadius.circular(borderRadius) : null,
      tiltConfig: tiltConfig ?? const TiltConfig(),
      lightConfig: lightConfig ?? const LightConfig(),
      shadowConfig: shadowConfig ?? const ShadowConfig(),
      childLayout: childLayout,
      // lightShadowMode: lightShadowMode, // Not available in current flutter_tilt version
      disable: disable,
      fps: fps,
      onGestureMove: (tiltDataModel, gesturesType) {
        widget.backend.triggerControlEvent(
          widget.control.id,
          "gesture_move",
          jsonEncode({
            "x": tiltDataModel.position.dx,
            "y": tiltDataModel.position.dy,
            "angle": tiltDataModel.angle,
            "gestures_type": gesturesType.name,
          }),
        );
      },
      onGestureLeave: (tiltDataModel, gesturesType) {
        widget.backend.triggerControlEvent(
          widget.control.id,
          "gesture_leave",
          jsonEncode({
            "x": tiltDataModel.position.dx,
            "y": tiltDataModel.position.dy,
            "angle": tiltDataModel.angle,
            "gestures_type": gesturesType.name,
          }),
        );
      },
      child: child ??
          Container(
            width: 100,
            height: 100,
            decoration: BoxDecoration(
              color: Colors.blue.shade300,
              borderRadius: BorderRadius.circular(8),
            ),
            child: const Center(
              child: Text(
                'Tilt',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
    );

    return constrainedControl(
        context, tiltWidget, widget.parent, widget.control);
  }

  TiltConfig? _parseTiltConfig() {
    final String? configJson = widget.control.attrString("tilt_config");
    if (configJson == null) return null;

    try {
      final Map<String, dynamic> config = jsonDecode(configJson);

      // Detect if platform supports sensors (only mobile platforms)
      bool isMobilePlatform = false;
      if (!kIsWeb) {
        isMobilePlatform = Platform.isAndroid || Platform.isIOS;
      }
      // Only enable sensors on mobile platforms
      bool enableSensors = config['enable_gesture_sensors'] ?? false;
      if (enableSensors && !isMobilePlatform) {
        enableSensors = false;
        debugPrint("Sensors disabled: Not a mobile platform");
      }
      return TiltConfig(
        disable: config['disable'] ?? false,
        initial: parseOffset(widget.control, 'initial'),
        angle: config['angle']?.toDouble() ?? 10.0,
        direction: _parseTiltDirectionList(config['direction']),
        enableReverse: config['enable_reverse'] ?? false,
        filterQuality: parseFilterQuality(config['filter_quality']) ?? FilterQuality.low,
        enableGestureSensors: config['enable_gesture_sensors'] ?? true,
        sensorFactor: config['sensor_factor']?.toDouble() ?? 10.0,
        enableSensorRevert: config['enable_sensor_revert'] ?? true,
        sensorRevertFactor: config['sensor_revert_factor']?.toDouble() ?? 0.05,
        sensorMoveDuration: parseDuration(widget.control, 'sensor_move_duration') ?? const Duration(milliseconds: 50),
        enableGestureHover: config['enable_gesture_hover'] ?? true,
        enableGestureTouch: config['enable_gesture_touch'] ?? true,
        enableRevert: config['enable_revert'] ?? true,
        enableOutsideAreaMove: config['enable_outside_area_move'] ?? true,
        moveDuration: parseDuration(widget.control, 'move_duration') ?? const Duration(milliseconds: 100),
        leaveDuration: parseDuration(widget.control, 'leave_duration') ?? const Duration(milliseconds: 300),
        moveCurve: parseCurve(config['move_curve']) ?? Curves.linear,
        leaveCurve: parseCurve(config['leave_curve']) ?? Curves.linear,
        controllerMoveDuration: parseDuration(widget.control, 'controller_move_duration') ?? const Duration(milliseconds: 100),
        controllerLeaveDuration: parseDuration(widget.control, 'controller_leave_duration') ?? const Duration(milliseconds: 300),
      );
    } catch (e) {
      debugPrint("Error parsing tiltConfig: $e");
      return null;
    }
  }

  LightConfig? _parseLightConfig() {
    final String? configJson = widget.control.attrString("light_config");
    if (configJson == null) return null;

    try {
      final Map<String, dynamic> config = jsonDecode(configJson);
      return LightConfig(
        color: parseColor(Theme.of(context), config['color']) ?? const Color(0xFFFFFFFF),
        minIntensity: config['min_intensity']?.toDouble() ?? 0.0,
        maxIntensity: config['max_intensity']?.toDouble() ?? 0.5,
        spreadFactor: config['spread_factor']?.toDouble() ?? 4.0,
        direction: _parseLightDirection(config['direction']),
        enableReverse: config['enable_reverse'] ?? false,
        disable: config['disable'] ?? false,
      );
    } catch (e) {
      debugPrint("Error parsing light_config: $e");
      return null;
    }
  }

  ShadowConfig? _parseShadowConfig() {
    final String? configJson = widget.control.attrString("shadow_config");
    if (configJson == null) return null;

    try {
      final Map<String, dynamic> config = jsonDecode(configJson);
      return ShadowConfig(
        color: parseColor(Theme.of(context), config['color']) ?? const Color(0xFF9E9E9E),
        minIntensity: config['min_intensity']?.toDouble() ?? 0.0,
        maxIntensity: config['max_intensity']?.toDouble() ?? 0.5,
        offsetInitial: parseOffset(widget.control, 'offset_initial') ?? Offset.zero,
        offsetFactor: config['offset_factor']?.toDouble() ?? 0.1,
        spreadInitial: config['spread_initial']?.toDouble() ?? 0.0,
        spreadFactor: config['spread_factor']?.toDouble() ?? 0.0,
        minBlurRadius: config['min_blur_radius']?.toDouble() ?? 0.0,
        maxBlurRadius: config['max_blur_radius']?.toDouble() ?? 10.0,
        direction: _parseShadowDirection(config['direction']),
        enableReverse: config['enable_reverse'] ?? false,
        disable: config['disable'] ?? false,
      );
    } catch (e) {
      debugPrint("Error parsing shadow_config: $e");
      return null;
    }
  }

  ChildLayout _parseChildLayout() {
    List<Widget> outerWidgets = [];
    List<Widget> innerWidgets = [];
    List<Widget> behindWidgets = [];

    // Parse child_layout_outer widgets
    var outerChildren = widget.children
        .where((c) => c.name == "child_layout_outer" && c.isVisible);
    for (final child in outerChildren) {
      final childWidget =
          createControl(widget.control, child.id, widget.control.isDisabled);

      // Outer layer positioned left=0 with positive offset (like Flutter example)
      outerWidgets.add(
        Positioned(
          left: 0,
          child: TiltParallax(
            size: const Offset(40, 40), // Positive values like Flutter example
            child: childWidget,
          ),
        ),
      );
    }

    // Parse child_layout_inner widgets
    var innerChildren = widget.children
        .where((c) => c.name == "child_layout_inner" && c.isVisible);
    for (final child in innerChildren) {
      final childWidget =
          createControl(widget.control, child.id, widget.control.isDisabled);

      // Inner layer positioned right=0 with negative offset (like Flutter example)
      innerWidgets.add(
        Positioned(
          right: 0,
          child: TiltParallax(
            size:
                const Offset(-40, -40), // Negative values like Flutter example
            child: childWidget,
          ),
        ),
      );
    }

    // Parse child_layout_behind widgets
    var behindChildren = widget.children
        .where((c) => c.name == "child_layout_behind" && c.isVisible);
    int behindIndex = 0;
    for (final child in behindChildren) {
      final childWidget =
          createControl(widget.control, child.id, widget.control.isDisabled);

      // Behind layers positioned like Flutter example
      if (behindIndex == 0) {
        // First behind layer: bottom=-10, offset=(-50, -50)
        behindWidgets.add(
          Positioned(
            bottom: -10,
            child: TiltParallax(
              size: const Offset(-50, -50),
              child: childWidget,
            ),
          ),
        );
      } else if (behindIndex == 1) {
        // Second behind layer: bottom=-5, offset=(-25, -25)
        behindWidgets.add(
          Positioned(
            bottom: -5,
            child: TiltParallax(
              size: const Offset(-25, -25),
              child: childWidget,
            ),
          ),
        );
      } else {
        // Additional behind layers with progressive offsets
        behindWidgets.add(
          Positioned(
            bottom: -5.0 + (behindIndex * 2.0),
            child: TiltParallax(
              size: Offset(
                  -25.0 + (behindIndex * 5.0), -25.0 + (behindIndex * 5.0)),
              child: childWidget,
            ),
          ),
        );
      }
      behindIndex++;
    }

    return ChildLayout(
      outer: outerWidgets,
      inner: innerWidgets,
      behind: behindWidgets,
    );
  }

  List<TiltDirection>? _parseTiltDirectionList(dynamic direction) {
    if (direction == null) return null;

    if (direction is String) {
      switch (direction) {
        case 'none':
          return [TiltDirection.none];
        case 'top':
          return [TiltDirection.top];
        case 'bottom':
          return [TiltDirection.bottom];
        case 'left':
          return [TiltDirection.left];
        case 'right':
          return [TiltDirection.right];
        case 'topLeft':
          return [TiltDirection.topLeft];
        case 'topRight':
          return [TiltDirection.topRight];
        case 'bottomLeft':
          return [TiltDirection.bottomLeft];
        case 'bottomRight':
          return [TiltDirection.bottomRight];
        case 'all':
          return [
            TiltDirection.top,
            TiltDirection.bottom,
            TiltDirection.left,
            TiltDirection.right
          ];
        default:
          return [TiltDirection.top, TiltDirection.bottom];
      }
    }

    if (direction is List) {
      List<TiltDirection> directions = [];
      for (var dir in direction) {
        if (dir is String) {
          switch (dir) {
            case 'none':
              directions.add(TiltDirection.none);
              break;
            case 'top':
              directions.add(TiltDirection.top);
              break;
            case 'bottom':
              directions.add(TiltDirection.bottom);
              break;
            case 'left':
              directions.add(TiltDirection.left);
              break;
            case 'right':
              directions.add(TiltDirection.right);
              break;
            case 'topLeft':
              directions.add(TiltDirection.topLeft);
              break;
            case 'topRight':
              directions.add(TiltDirection.topRight);
              break;
            case 'bottomLeft':
              directions.add(TiltDirection.bottomLeft);
              break;
            case 'bottomRight':
              directions.add(TiltDirection.bottomRight);
              break;
          }
        } else if (dir is Map<String, dynamic>) {
          // Support for custom TiltDirection(x, y)
          double x = dir['x']?.toDouble() ?? 0.0;
          double y = dir['y']?.toDouble() ?? 0.0;
          directions.add(TiltDirection(x, y));
        }
      }
      return directions.isNotEmpty ? directions : null;
    }

    return null;
  }

  LightDirection _parseLightDirection(String? direction) {
    switch (direction) {
      case 'around':
        return LightDirection.around;
      case 'center':
        return LightDirection.center;
      case 'all':
        return LightDirection.all;
      default:
        return LightDirection.around;
    }
  }

  ShadowDirection _parseShadowDirection(String? direction) {
    switch (direction) {
      case 'around':
        return ShadowDirection.around;
      case 'center':
        return ShadowDirection.center;
      case 'all':
        return ShadowDirection.all;
      default:
        return ShadowDirection.around;
    }
  }

  Map<String, dynamic> _parseParallaxConfig() {
    final String? configJson = widget.control.attrString("parallax_config");
    if (configJson == null) {
      return {}; // Return empty map with default values
    }

    try {
      return jsonDecode(configJson);
    } catch (e) {
      debugPrint("Error parsing parallax_config: $e");
      return {};
    }
  }

  // Custom parsing functions removed - now using Flet's built-in parsing utilities
}
