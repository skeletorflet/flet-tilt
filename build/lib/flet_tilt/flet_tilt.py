from enum import Enum
from typing import Any, Optional, Union, List

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber, Control
from flet.core.ref import Ref
from flet.core.types import OptionalControlEventCallable, Duration, DurationValue
from flet.core.animation import AnimationCurve

class TiltDirection(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    TOP_LEFT = "topLeft"
    TOP_RIGHT = "topRight"
    BOTTOM_LEFT = "bottomLeft"
    BOTTOM_RIGHT = "bottomRight"
    CENTER = "center"
    NONE = "none"

class GesturesType(Enum):
    NONE = "none"
    TOUCH = "touch"
    HOVER = "hover"
    CONTROLLER = "controller"
    SENSORS = "sensors"

class LightDirection(Enum):
    AROUND = "around"
    CENTER = "center"
    ALL = "all"

class ShadowDirection(Enum):
    AROUND = "around"
    CENTER = "center"
    ALL = "all"

class LightShadowMode(Enum):
    PROJECTOR = "projector"
    PERFORMANCE = "performance"

class TiltConfig:
    """
    Configuration class for tilt behavior.
    
    Controls how the widget responds to gestures and the intensity of the tilt effect.
    """
    
    def __init__(
        self,
        disable: Optional[bool] = None,
        initial: Optional[Union[float, tuple]] = None,
        angle: Optional[float] = None,
        direction: Optional[List[Union[TiltDirection, str]]] = None,
        enable_revert: Optional[bool] = None,
        filter_quality: Optional[str] = None,
        enable_gesture_sensors: Optional[bool] = None,
        sensor_factor: Optional[float] = None,
        enable_sensor_revert: Optional[bool] = None,
        sensor_revert_factor: Optional[float] = None,
        sensor_move_duration: Optional[DurationValue] = None,
        enable_gesture_hover: Optional[bool] = None,
        enable_gesture_touch: Optional[bool] = None,
        enable_outside_area_move: Optional[bool] = None,
        move_duration: Optional[DurationValue] = None,
        leave_duration: Optional[DurationValue] = None,
        move_curve: Optional[Union[AnimationCurve, str]] = None,
        leave_curve: Optional[Union[AnimationCurve, str]] = None,
        controller_move_duration: Optional[DurationValue] = None,
        controller_leave_duration: Optional[DurationValue] = None,
    ):
        """
        Initialize TiltConfig.
        
        Args:
            disable: Disable tilt effect
            initial: Initial tilt value (float or tuple)
            angle: Tilt angle in degrees (0.0 to 1.0)
            direction: Allowed tilt directions
            enable_revert: Enable revert direction
            filter_quality: Filter quality (none, low, medium, high)
            enable_gesture_sensors: Enable gesture sensors (mobile only)
            sensor_factor: Sensor sensitivity factor
            enable_sensor_revert: Enable sensor revert
            sensor_revert_factor: Sensor revert factor (0.0 to 1.0)
            sensor_move_duration: Sensor move duration (Duration or milliseconds)
            enable_gesture_hover: Enable hover gestures
            enable_gesture_touch: Enable touch gestures
            enable_outside_area_move: Enable outside area move
            move_duration: Move animation duration (Duration or milliseconds)
            leave_duration: Leave animation duration (Duration or milliseconds)
            move_curve: Move animation curve (AnimationCurve or string)
            leave_curve: Leave animation curve (AnimationCurve or string)
            controller_move_duration: Controller move duration (Duration or milliseconds)
            controller_leave_duration: Controller leave duration (Duration or milliseconds)
        """
        self.disable = disable
        self.initial = initial
        self.angle = angle
        self.direction = direction
        self.enable_revert = enable_revert
        self.filter_quality = filter_quality
        self.enable_gesture_sensors = enable_gesture_sensors
        self.sensor_factor = sensor_factor
        self.enable_sensor_revert = enable_sensor_revert
        self.sensor_revert_factor = sensor_revert_factor
        self.sensor_move_duration = sensor_move_duration
        self.enable_gesture_hover = enable_gesture_hover
        self.enable_gesture_touch = enable_gesture_touch
        self.enable_outside_area_move = enable_outside_area_move
        self.move_duration = move_duration
        self.leave_duration = leave_duration
        self.move_curve = move_curve
        self.leave_curve = leave_curve
        self.controller_move_duration = controller_move_duration
        self.controller_leave_duration = controller_leave_duration
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        def duration_to_dict(duration):
            if isinstance(duration, Duration):
                return {
                    "milliseconds": duration.milliseconds,
                    "seconds": duration.seconds,
                    "minutes": duration.minutes,
                    "hours": duration.hours,
                    "days": duration.days,
                    "microseconds": duration.microseconds,
                }
            return duration
        
        return {
            "disable": self.disable,
            "initial": self.initial,
            "angle": self.angle,
            "direction": [d.value if hasattr(d, 'value') else d for d in self.direction] if isinstance(self.direction, list) else (self.direction.value if hasattr(self.direction, 'value') else self.direction),
            "enable_revert": self.enable_revert,
            "filter_quality": self.filter_quality,
            "enable_gesture_sensors": self.enable_gesture_sensors,
            "sensor_factor": self.sensor_factor,
            "enable_sensor_revert": self.enable_sensor_revert,
            "sensor_revert_factor": self.sensor_revert_factor,
            "sensor_move_duration": duration_to_dict(self.sensor_move_duration),
            "enable_gesture_hover": self.enable_gesture_hover,
            "enable_gesture_touch": self.enable_gesture_touch,
            "enable_outside_area_move": self.enable_outside_area_move,
            "move_duration": duration_to_dict(self.move_duration),
            "leave_duration": duration_to_dict(self.leave_duration),
            "move_curve": self.move_curve.value if hasattr(self.move_curve, 'value') else self.move_curve,
            "leave_curve": self.leave_curve.value if hasattr(self.leave_curve, 'value') else self.leave_curve,
            "controller_move_duration": duration_to_dict(self.controller_move_duration),
            "controller_leave_duration": duration_to_dict(self.controller_leave_duration),
        }

class LightConfig:
    """
    Configuration class for light effects.
    
    Controls the appearance and behavior of light effects during tilt.
    """
    
    def __init__(
        self,
        disable: Optional[bool] = None,
        color: Optional[str] = None,
        min_intensity: Optional[float] = None,
        max_intensity: Optional[float] = None,
        spread_factor: Optional[float] = None,
        direction: Optional[Union[LightDirection, str]] = None,
        enable_reverse: Optional[bool] = None,
    ):
        """
        Initialize LightConfig.
        
        Args:
            disable: Disable light effect
            color: Light color (hex string)
            min_intensity: Minimum light intensity (0.0 to 1.0)
            max_intensity: Maximum light intensity (0.0 to 1.0)
            spread_factor: Light spread factor
            direction: Light direction
            enable_reverse: Enable reverse light direction
        """
        self.disable = disable
        self.color = color
        self.min_intensity = min_intensity
        self.max_intensity = max_intensity
        self.spread_factor = spread_factor
        self.direction = direction
        self.enable_reverse = enable_reverse
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'value'):
                    result[key] = value.value
                else:
                    result[key] = value
        return result

class ShadowConfig:
    """
    Configuration class for shadow effects.
    
    Controls the appearance and behavior of shadow effects during tilt.
    """
    
    def __init__(
        self,
        disable: Optional[bool] = None,
        color: Optional[str] = None,
        min_intensity: Optional[float] = None,
        max_intensity: Optional[float] = None,
        offset_initial: Optional[float] = None,
        offset_factor: Optional[float] = None,
        spread_initial: Optional[float] = None,
        spread_factor: Optional[float] = None,
        min_blur_radius: Optional[float] = None,
        max_blur_radius: Optional[float] = None,
        direction: Optional[Union[ShadowDirection, str]] = None,
        enable_reverse: Optional[bool] = None,
    ):
        """
        Initialize ShadowConfig.
        
        Args:
            disable: Disable shadow effect
            color: Shadow color (hex string)
            min_intensity: Minimum shadow intensity (0.0 to 1.0)
            max_intensity: Maximum shadow intensity (0.0 to 1.0)
            offset_initial: Initial shadow offset
            offset_factor: Shadow offset factor
            spread_initial: Initial shadow spread
            spread_factor: Shadow spread factor
            min_blur_radius: Minimum blur radius
            max_blur_radius: Maximum blur radius
            direction: Shadow direction
            enable_reverse: Enable reverse shadow direction
        """
        self.disable = disable
        self.color = color
        self.min_intensity = min_intensity
        self.max_intensity = max_intensity
        self.offset_initial = offset_initial
        self.offset_factor = offset_factor
        self.spread_initial = spread_initial
        self.spread_factor = spread_factor
        self.min_blur_radius = min_blur_radius
        self.max_blur_radius = max_blur_radius
        self.direction = direction
        self.enable_reverse = enable_reverse
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'value'):
                    result[key] = value.value
                else:
                    result[key] = value
        return result

class ParallaxConfig:
    """
    Configuration class for parallax effects.
    
    Controls the parallax movement of child elements during tilt.
    """
    
    def __init__(
        self,
        disable: Optional[bool] = None,
        factor: Optional[float] = None,
    ):
        """
        Initialize ParallaxConfig.
        
        Args:
            disable: Disable parallax effect
            factor: Parallax movement factor (0.0 to 1.0)
        """
        self.disable = disable
        self.factor = factor
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                result[key] = value
        return result

class FletTilt(ConstrainedControl):
    """
    FletTilt Control - A Flutter Tilt widget wrapper for Flet.
    
    Provides tilt effects with light, shadow, and parallax animations.
    Supports touch, hover, controller, and sensor gestures.
    """

    def __init__(
        self,
        #
        # Control
        #
        ref: Optional[Ref] = None,
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        #
        # FletTilt specific
        #
        child: Optional[Control] = None,
        border_radius: OptionalNumber = None,
        tilt_config: Optional[Union[TiltConfig, dict]] = None,
        light_config: Optional[Union[LightConfig, dict]] = None,
        shadow_config: Optional[Union[ShadowConfig, dict]] = None,
        child_layout_outer: Optional[List[Control]] = None,
        child_layout_inner: Optional[List[Control]] = None,
        child_layout_behind: Optional[List[Control]] = None,
        parallax_config: Optional[Union[ParallaxConfig, dict]] = None,
        light_shadow_mode: Optional[Union[LightShadowMode, str]] = None,
        disable: Optional[bool] = None,
        fps: Optional[int] = None,
        on_gesture_move: OptionalControlEventCallable = None,
        on_gesture_leave: OptionalControlEventCallable = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            width=width,
            height=height,
        )

        self.child = child
        self.border_radius = border_radius
        self.tilt_config = tilt_config
        self.light_config = light_config
        self.shadow_config = shadow_config
        self.child_layout_outer = child_layout_outer
        self.child_layout_inner = child_layout_inner
        self.child_layout_behind = child_layout_behind
        self.parallax_config = parallax_config
        self.light_shadow_mode = light_shadow_mode
        self.disable = disable
        self.fps = fps
        self.on_gesture_move = on_gesture_move
        self.on_gesture_leave = on_gesture_leave

    def _get_control_name(self):
        return "flet_tilt"

    def _get_children(self):
        children = []
        if self.child:
            children.append(self.child)
        if self.child_layout_outer:
            for control in self.child_layout_outer:
                control._set_attr_internal("n", "child_layout_outer")
                children.append(control)
        if self.child_layout_inner:
            for control in self.child_layout_inner:
                control._set_attr_internal("n", "child_layout_inner")
                children.append(control)
        if self.child_layout_behind:
            for control in self.child_layout_behind:
                control._set_attr_internal("n", "child_layout_behind")
                children.append(control)
        return children

    def before_update(self):
        super().before_update()
        # Convert config objects to dictionaries if needed
        tilt_dict = self.__tilt_config.to_dict() if isinstance(self.__tilt_config, TiltConfig) else self.__tilt_config
        light_dict = self.__light_config.to_dict() if isinstance(self.__light_config, LightConfig) else self.__light_config
        shadow_dict = self.__shadow_config.to_dict() if isinstance(self.__shadow_config, ShadowConfig) else self.__shadow_config
        parallax_dict = self.__parallax_config.to_dict() if isinstance(self.__parallax_config, ParallaxConfig) else self.__parallax_config
        
        self._set_attr_json("tilt_config", tilt_dict)
        self._set_attr_json("light_config", light_dict)
        self._set_attr_json("shadow_config", shadow_dict)
        self._set_attr_json("parallax_config", parallax_dict)

    # child
    @property
    def child(self) -> Optional[Control]:
        return self.__child

    @child.setter
    def child(self, value: Optional[Control]):
        self.__child = value

    # border_radius
    @property
    def border_radius(self) -> OptionalNumber:
        return self._get_attr("borderRadius")

    @border_radius.setter
    def border_radius(self, value: OptionalNumber):
        self._set_attr("borderRadius", value)

    # tilt_config
    @property
    def tilt_config(self) -> Optional[Union[TiltConfig, dict]]:
        return self.__tilt_config

    @tilt_config.setter
    def tilt_config(self, value: Optional[Union[TiltConfig, dict]]):
        self.__tilt_config = value

    # light_config
    @property
    def light_config(self) -> Optional[Union[LightConfig, dict]]:
        return self.__light_config

    @light_config.setter
    def light_config(self, value: Optional[Union[LightConfig, dict]]):
        self.__light_config = value

    # shadow_config
    @property
    def shadow_config(self) -> Optional[Union[ShadowConfig, dict]]:
        return self.__shadow_config

    @shadow_config.setter
    def shadow_config(self, value: Optional[Union[ShadowConfig, dict]]):
        self.__shadow_config = value

    # parallax_config
    @property
    def parallax_config(self) -> Optional[Union[ParallaxConfig, dict]]:
        return self.__parallax_config

    @parallax_config.setter
    def parallax_config(self, value: Optional[Union[ParallaxConfig, dict]]):
        self.__parallax_config = value

    # child_layout_outer
    @property
    def child_layout_outer(self) -> Optional[List[Control]]:
        return self.__child_layout_outer

    @child_layout_outer.setter
    def child_layout_outer(self, value: Optional[List[Control]]):
        self.__child_layout_outer = value

    # child_layout_inner
    @property
    def child_layout_inner(self) -> Optional[List[Control]]:
        return self.__child_layout_inner

    @child_layout_inner.setter
    def child_layout_inner(self, value: Optional[List[Control]]):
        self.__child_layout_inner = value

    # child_layout_behind
    @property
    def child_layout_behind(self) -> Optional[List[Control]]:
        return self.__child_layout_behind

    @child_layout_behind.setter
    def child_layout_behind(self, value: Optional[List[Control]]):
        self.__child_layout_behind = value

    # disable
    @property
    def disable(self) -> Optional[bool]:
        return self._get_attr("disable")

    @disable.setter
    def disable(self, value: Optional[bool]):
        self._set_attr("disable", value)

    # fps
    @property
    def fps(self) -> Optional[int]:
        return self._get_attr("fps")

    @fps.setter
    def fps(self, value: Optional[int]):
        self._set_attr("fps", value)

    # light_shadow_mode
    @property
    def light_shadow_mode(self) -> Optional[Union[LightShadowMode, str]]:
        return self._get_attr("lightShadowMode")

    @light_shadow_mode.setter
    def light_shadow_mode(self, value: Optional[Union[LightShadowMode, str]]):
        if isinstance(value, LightShadowMode):
            self._set_attr("lightShadowMode", value.value)
        else:
            self._set_attr("lightShadowMode", value)

    # on_gesture_move
    @property
    def on_gesture_move(self) -> OptionalControlEventCallable:
        return self._get_event_handler("gesture_move")

    @on_gesture_move.setter
    def on_gesture_move(self, handler: OptionalControlEventCallable):
        self._add_event_handler("gesture_move", handler)

    # on_gesture_leave
    @property
    def on_gesture_leave(self) -> OptionalControlEventCallable:
        return self._get_event_handler("gesture_leave")

    @on_gesture_leave.setter
    def on_gesture_leave(self, handler: OptionalControlEventCallable):
        self._add_event_handler("gesture_leave", handler)
