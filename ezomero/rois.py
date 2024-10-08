from dataclasses import dataclass, field
from typing import List, Tuple, Union

__all__ = ["Point",
           "Line",
           "Rectangle",
           "Ellipse",
           "Polygon",
           "Polyline",
           "Label",
           "ezShape",
           "AffineTransform"]


@dataclass(frozen=True)
class AffineTransform():
    """A dataclss for affine transformation matrix of shapes"""
    a00: float = field(default=1.0)
    a10: float = field(default=0.0)
    a01: float = field(default=0.0)
    a11: float = field(default=1.0)
    a02: float = field(default=0.0)
    a12: float = field(default=0.0)


@dataclass(frozen=True)
class ezShape:
    """Generic dataclass used to create an OMERO Shape.

    A dataclass used to represent any shape and create an OMERO equivalent.
    This class has no fields; it's just extended by all ROIs.
    This dataclass is frozen and should not be modified after instantiation

    """
    transform: Union[AffineTransform, None] = field(default=None, kw_only=True)


@dataclass(frozen=True)
class Point(ezShape):
    """A dataclass used to create an OMERO Point.

    A dataclass used to represent a Point shape and create an OMERO equivalent.
    This dataclass is frozen and should not be modified after instantiation

    Parameters
    ----------
    x : float
        The x axis position of the point shape in pixels.
    y : float
        The y axis position of the point shape in pixels.
    z : int, optional
        The z position of the point in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the Point will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the Point will not be linked to any time frame.
        Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    x: float = field(metadata={'units': 'PIXELS'})
    y: float = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Line(ezShape):
    """A dataclass used to create an OMERO Line.

    A dataclass used to represent a Line shape and create an OMERO equivalent.
    This dataclass is frozen and should not be modified after instantiation.

    Parameters
    ----------
    x1 : float
        The x axis position of the start point of the line shape in pixels.
    y1 : float
        The y axis position of the start point of the line shape in pixels.
    x2 : float
        The x axis position of the end point of the line shape in pixels.
    y2 : float
        The y axis position of the end point of the line shape in pixels.
    z : int, optional
        The z position of the shape in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the shape will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the shape will not be linked to any time frame.
        Default is ``None``.
    markerStart : str, optional
        The marker for the start of the line. Default is ``None``.
    markerEnd : str, optional
        The marker for the end of the line. Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    x1: float = field(metadata={'units': 'PIXELS'})
    y1: float = field(metadata={'units': 'PIXELS'})
    x2: float = field(metadata={'units': 'PIXELS'})
    y2: float = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    markerStart: Union[str, None] = field(default=None)
    markerEnd: Union[str, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Rectangle(ezShape):
    """A dataclass used to create an OMERO rectangle.

    A dataclass used to represent a Rectangle shape and create an OMERO
    equivalent. This dataclass is frozen and should not be modified after
    instantiation.

    Parameters
    ----------
    x : float
        The x axis position of the rectangle shape in pixels.
    y : float
        The y axis position of the rectangle shape in pixels.
    width : float
        The width (x axis) of the rectangle shape in pixels.
    height : float
        The height (y axis) of the rectangle shape in pixels.
    z : int, optional
        The z position of the shape in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the shape will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the shape will not be linked to any time frame.
        Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    x: float = field(metadata={'units': 'PIXELS'})
    y: float = field(metadata={'units': 'PIXELS'})
    width: float = field(metadata={'units': 'PIXELS'})
    height: float = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Ellipse(ezShape):
    """A dataclass used to create an OMERO Ellipse.

    A dataclass used to represent an Ellipse shape and create an OMERO
    equivalent. This dataclass is frozen and should not be modified after
    instantiation.

    Parameters
    ----------
    x : float
        The x axis position of the ellipse shape in pixels.
    y : float
        The y axis position of the ellipse shape in pixels.
    x_rad : float
        The x radius of the ellipse shape in pixels.
    y_rad : float
        The y radius of the ellipse shape in pixels.
    z : int, optional
        The z position of the shape in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the shape will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the shape will not be linked to any time frame.
        Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    x: float = field(metadata={'units': 'PIXELS'})
    y: float = field(metadata={'units': 'PIXELS'})
    x_rad: float = field(metadata={'units': 'PIXELS'})
    y_rad: float = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Polygon(ezShape):
    """A dataclass used to create an OMERO polygon.

    A dataclass used to represent a Polygon shape and create an OMERO
    equivalent. This dataclass is frozen and should not be modified after
    instantiation.

    Parameters
    ----------
    points : list of tuples of 2 floats
        A list of 2 element tuples corresponding to the (x, y) coordinates of
        each vertex of the polygon.
    z : int, optional
        The z position of the shape in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the shape will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the shape will not be linked to any time frame.
        Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    points: List[Tuple[float, float]] = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Polyline(ezShape):
    """A dataclass used to create an OMERO polyline.

    A dataclass used to represent a Polyline shape and create an OMERO
    equivalent. This dataclass is frozen and should not be modified after
    instantiation.

    Parameters
    ----------
    points : list of tuples of 2 floats
        A list of 2 element tuples corresponding to the (x, y) coordinates of
        each vertex of the polyline.
    z : int, optional
        The z position of the shape in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Point will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the shape will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the shape will not be linked to any time frame.
        Default is ``None``.
    label : str, optional
        The label of the shape. Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    points: List[Tuple[float, float]] = field(metadata={'units': 'PIXELS'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    label: Union[str, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)


@dataclass(frozen=True)
class Label(ezShape):
    """A dataclass used to create an OMERO Label.

    A dataclass used to represent a Label shape and create an OMERO equivalent.
    This dataclass is frozen and should not be modified after instantiation

    Parameters
    ----------
    x : float
        The x axis position of the label shape in pixels.
    y : float
        The y axis position of the label shape in pixels.
    label : str
        The text value of the Label.
    fontSize: int
        The font size of the label, in pt.
    z : int, optional
        The z position of the label in pixels. Note this is the z plane to
        which the shape is linked and not the sub-voxel resolution position of
        your shape. If ``None``, the Label will not be linked to any z plane.
        Default is ``None``.
    c : int, optional
        The channel index to which the shape is linked.
        If None, the Label will not be linked to any channel. Default is
        ``None``.
    t : int, optional
        The time frame to which the shape is linked.
        If ``None``, the Label will not be linked to any time frame.
        Default is ``None``.
    fill_color : Tuple (4 integers), optional
        The color that will be used as the fill/background of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (0, 0, 0, 0) (i.e. transparent) in
        ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_color : Tuple (4 integers), optional
        The color that will be used as the stroke/perimeter of this Shape.
        Format is RGBA, 0-255.
        If ``None``, we default to (255, 255, 0, 255) (i.e. yellow, following
        OMERO.iViewer default) in ``ezomero.get_shape()``.
        Default is ``None``.
    stroke_width : float, optional
        The line width used for the stroke/perimeter of this Shape.
        If ``None``, we default to 1.0 in ``ezomero.get_shape()``.
        Default is ``None``.
    """

    x: float = field(metadata={'units': 'PIXELS'})
    y: float = field(metadata={'units': 'PIXELS'})
    label: str = field()
    fontSize: int = field(metadata={'FontSizeUnit': 'pt'})
    z: Union[int, None] = field(default=None)
    c: Union[int, None] = field(default=None)
    t: Union[int, None] = field(default=None)
    fill_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_color: Union[Tuple[int, int, int, int], None] = field(default=None)
    stroke_width: Union[float, None] = field(default=None)
