"""
Constants and Predefined Data Tables
====================================

This module defines or loads all of the constants and predefined data tables
included in the VC-2 specification documents themselves.

"""

from enum import IntEnum

from collections import namedtuple

from vc2_data_tables.csv_readers import (
    read_enum_from_csv,
    read_lookup_from_csv,
    read_quantisation_matrices_from_csv,
    to_list,
    to_enum_from_index,
    to_enum_from_name,
    to_dict_value,
)

__all__ = [
    "PARSE_INFO_PREFIX",
    "PARSE_INFO_HEADER_BYTES",
    "ParseCodes",
    "PictureCodingModes",
    "ColorDifferenceSamplingFormats",
    "SourceSamplingModes",
    "PresetFrameRates",
    "FrameRate",
    "PRESET_FRAME_RATES",
    "PresetPixelAspectRatios",
    "PixelAspectRatio",
    "PRESET_PIXEL_ASPECT_RATIOS",
    "PresetSignalRanges",
    "SignalRangeParameters",
    "PRESET_SIGNAL_RANGES",
    "PresetColorPrimaries",
    "ColorPrimariesParameters",
    "PRESET_COLOR_PRIMARIES",
    "PresetColorMatrices",
    "ColorMatrixParameters",
    "PRESET_COLOR_MATRICES",
    "PresetTransferFunctions",
    "TransferFunctionParameters",
    "PRESET_TRANSFER_FUNCTIONS",
    "ColorSpecificiation",
    "PresetColorSpecs",
    "PRESET_COLOR_SPECS",
    "BaseVideoFormats",
    "BaseVideoFormatParameters",
    "BASE_VIDEO_FORMAT_PARAMETERS",
    "LiftingFilterTypes",
    "WaveletFilters",
    "LiftingStage",
    "LiftingFilterParameters",
    "LIFTING_FILTERS",
    "Profiles",
    "ProfileParameters",
    "PROFILES",
    "QUANTISATION_MATRICES",
    "Levels",
    "LEVELS",
]

################################################################################
# (10.5) Parse Info Block
################################################################################

PARSE_INFO_PREFIX = 0x42424344
"""
(10.5.1) The 'magic bytes' used to identify the start of a parse info header.
'BBCD' in ASCII.
"""

PARSE_INFO_HEADER_BYTES = 13
"""(10.5.1) The number of bytes in the parse_info header."""

class ParseCodes(IntEnum):
    """
    (10.5.2) Valid parse_code values from (Table 10.1). Names are not normative.
    """
    # VC-2 Syntax
    sequence_header = 0x00
    end_of_sequence = 0x10
    auxiliary_data = 0x20
    padding_data = 0x30
    
    # Pictures
    low_delay_picture = 0xC8
    high_quality_picture = 0xE8
    
    # Picture fragments
    low_delay_picture_fragment = 0xCC
    high_quality_picture_fragment = 0xEC


################################################################################
# (11) Picture coding mode identifiers
################################################################################

class PictureCodingModes(IntEnum):
    """(11.5) Indices defined in the text. Names are not normative."""
    pictures_are_frames = 0
    pictures_are_fields = 1

class ColorDifferenceSamplingFormats(IntEnum):
    """(11.4.4) Indices from (Table 11.2)"""
    
    color_4_4_4 = 0
    color_4_2_2 = 1
    color_4_2_0 = 2


class SourceSamplingModes(IntEnum):
    """(11.4.5) Indices defined in the text. Names are not normative."""
    progressive = 0
    interlaced = 1


################################################################################
# (11.4.6) Preset frame rates
################################################################################

FrameRate = namedtuple("FrameRate", "numerator,denominator")
"""
(11.4.6) A frame rate numerator and denominator value from (Table 11.1).

Parameters
----------
numerator : int
denominator : int
"""

PresetFrameRates = (
    read_enum_from_csv("preset_frame_rates.csv", "PresetFrameRates")
)
"""
(11.4.6) Preset framerate indices from (Table 11.1).
"""

PRESET_FRAME_RATES = (
    read_lookup_from_csv(
        "preset_frame_rates.csv",
        PresetFrameRates,
        FrameRate,
        type_conversions={
            "numerator": int,
            "denominator": int,
        },
    )
)
"""
(11.4.6) Frame-rate presets from (Table 11.3) indexed by
:py:class:`~.PresetFrameRates`.
"""


################################################################################
# (11.4.7) Preset pixel aspect ratios
################################################################################

PresetPixelAspectRatios = (
    read_enum_from_csv("preset_pixel_aspect_ratios.csv", "PresetPixelAspectRatios")
)
"""(11.4.7) Pixel aspect ratio preset indices from (Table 11.4)."""

PixelAspectRatio = namedtuple("PixelAspectRatio", "numerator,denominator")
"""(11.4.7) Pixel aspect ratio preset indices from (Table 11.4)."""

PRESET_PIXEL_ASPECT_RATIOS = (
    read_lookup_from_csv(
        "preset_pixel_aspect_ratios.csv",
        PresetPixelAspectRatios,
        PixelAspectRatio,
        type_conversions={
            "numerator": int,
            "denominator": int,
        },
    )
)
"""
(11.4.7) Pixel aspect ratio presets from (Table 11.4) indexed by
:py:class:`~.PresetPixelAspectRatios`
"""


################################################################################
# (11.4.9) Signal ranges
################################################################################

PresetSignalRanges = (
    read_enum_from_csv("preset_signal_ranges.csv", "PresetSignalRanges")
)
"""(11.4.9) Signal offsets/ranges preset indices from (Table 11.5)."""


SignalRangeParameters = namedtuple("SignalRangeParameters", "luma_offset,luma_excursion,color_diff_offset,color_diff_excursion")
"""
An entry in (Table 11.5).

Parameters
----------
luma_offset
    The luma value corresponding with 0.
luma_excursion
    The maximum value of an offset luma value.
color_diff_offset
    The color difference value corresponding with 0.
color_diff_excursion
    The maximum value of an offset color difference value.
"""

PRESET_SIGNAL_RANGES = (
    read_lookup_from_csv(
        "preset_signal_ranges.csv",
        PresetSignalRanges,
        SignalRangeParameters,
        type_conversions={
            "luma_offset": int,
            "luma_excursion": int,
            "color_diff_offset": int,
            "color_diff_excursion": int,
        },
    )
)
"""
(11.4.9) Signal offsets/ranges presets from (Table 11.5) indexed by
:py:class:`~.PresetSignalRanges`.
"""

################################################################################
# (11.4.10.2) Color Primaries
################################################################################

PresetColorPrimaries = (
    read_enum_from_csv("preset_color_primaries.csv", "PresetColorPrimaries")
)
"""(11.4.10.2) Color primaries from (Table 11.7)."""

ColorPrimariesParameters = namedtuple("ColorPrimariesParameters", "specification,")
"""
(11.4.10.2) A color primaries description.

Parameters
==========
specification : str
    The name of the specification defining the primaries in use.
"""

PRESET_COLOR_PRIMARIES = (
    read_lookup_from_csv(
        "preset_color_primaries.csv",
        PresetColorPrimaries,
        ColorPrimariesParameters,
    )
)
"""
(11.4.10.2) Normative specification names for color primaries from (Table 11.7)
indexed by :py:class:`~.PresetColorPrimaries`.
"""


################################################################################
# (11.4.10.3) Color Matrices
################################################################################

PresetColorMatrices = (
    read_enum_from_csv("preset_color_matrices.csv", "PresetColorMatrices")
)
"""(11.4.10.3) Color matrices from (Table 11.8)."""

ColorMatrixParameters = namedtuple("ColorMatrixParameters", "specification,color_matrix")
"""
An entry in (Table 11.8)

Parameters
----------
specification
    Normative specification name.
color_matrix
    Normative color matrix description.
"""

PRESET_COLOR_MATRICES = (
    read_lookup_from_csv(
        "preset_color_matrices.csv",
        PresetColorMatrices,
        ColorMatrixParameters,
    )
)
"""
(11.4.10.3) Color matrices from (Table 11.8) indexed by
:py:class:`~.PresetColorMatrices`.
"""

################################################################################
# (11.4.10.4) Transfer functions
################################################################################

PresetTransferFunctions = (
    read_enum_from_csv("preset_transfer_functions.csv", "PresetTransferFunctions")
)
"""(11.4.10.4) Transfer functions from (Table 11.9)."""

TransferFunctionParameters = namedtuple("TransferFunctionParameters", "specification,")
"""
An entry in (Table 11.9)

Parameters
----------
specification
    Normative specification name.
"""

PRESET_TRANSFER_FUNCTIONS = (
    read_lookup_from_csv(
        "preset_transfer_functions.csv",
        PresetTransferFunctions,
        TransferFunctionParameters,
    )
)
"""
(11.4.10.3) Color matrices from (Table 11.8) indexed by
:py:class:`~.PresetTransferFunctions`.
"""

################################################################################
# (11.4.10.1) Colour specifications
################################################################################

PresetColorSpecs = (
    read_enum_from_csv("preset_color_specs.csv", "PresetColorSpecs")
)
"""(11.4.10.1) Preset color specification collections from (Table 11.6)."""

ColorSpecificiation = namedtuple("ColorSpecificiation", "color_primaries_index,color_matrix_index,transfer_function_index")
"""
An entry in (Table 11.6)

Parameters
----------
color_primaries
    A :py:class:`~.PresetColorPrimaries` index.
color_matrix
    A :py:class:`~.PresetColorMatrices` index.
transfer_function
    A :py:class:`~.PresetTransferFunctions` index.
"""

PRESET_COLOR_SPECS = (
    read_lookup_from_csv(
        "preset_color_specs.csv",
        PresetColorSpecs,
        ColorSpecificiation,
        type_conversions={
            "color_primaries_index": to_enum_from_name(PresetColorPrimaries),
            "color_matrix_index": to_enum_from_name(PresetColorMatrices),
            "transfer_function_index": to_enum_from_name(PresetTransferFunctions),
        },
    )
)
"""
(11.4.10.3) Color matrices from (Table 11.8) indexed by
:py:class:`~.PresetTransferFunctions`.
"""


################################################################################
# (11.3) Base Video Formats
################################################################################

BaseVideoFormats = (
    read_enum_from_csv("base_video_format_parameters.csv", "BaseVideoFormats")
)
"""(11.3) Base video format indices from (Table 11.1)."""

BaseVideoFormatParameters = namedtuple("BaseVideoFormatParameters",
    "frame_width,"
    "frame_height,"
    "color_diff_format_index,"
    "source_sampling,"
    "top_field_first,"
    "frame_rate_index,"
    "pixel_aspect_ratio_index,"
    "clean_width,"
    "clean_height,"
    "left_offset,"
    "top_offset,"
    "signal_range_index,"
    "color_spec_index,"
)
"""
(B) An entry in (Table B.1a, B.1b or B.1c)

Parameters
----------
frame_width
frame_height
color_diff_format_index
    An entry from the enum :py:class:`~.ColorDifferenceSamplingFormats`. Listed
    as 'color difference sampling format' in (Table B.1).
source_sampling
    An entry from the enum :py:class:`~.SourceSamplingModes`. Specifies
    progressive or interlaced.
top_field_first
    If True, the top-line of the frame is in the first field.
frame_rate_index
    The frame rate, one of the indices of PRESET_FRAME_RATES.
pixel_aspect_ratio_index
    The pixel aspect ratio, an entry from the enum :py:class`~.PresetPixelAspectRatios`.
clean_width
clean_height
left_offset
top_offset
    The clean area of the pictures. See (11.4.8) and (E.4.2).
signal_range_index
    The signal ranges, an entry from the enum :py:class:`~.PresetSignalRanges`.
color_spec_index
    The color specification, an entry from the enum :py:class:`~.PresetColorSpecs`.
"""

BASE_VIDEO_FORMAT_PARAMETERS = (
    read_lookup_from_csv(
        "base_video_format_parameters.csv",
        BaseVideoFormats,
        BaseVideoFormatParameters,
        type_conversions={
            "frame_width": int,
            "frame_height": int,
            "color_diff_format_index": to_dict_value({
                "4:4:4": ColorDifferenceSamplingFormats.color_4_4_4,
                "4:2:2": ColorDifferenceSamplingFormats.color_4_2_2,
                "4:2:0": ColorDifferenceSamplingFormats.color_4_2_0,
            }),
            "source_sampling": to_enum_from_index(SourceSamplingModes),
            "top_field_first": to_dict_value({"TRUE": True, "FALSE": False}),
            "frame_rate_index": to_enum_from_index(PresetFrameRates),
            "pixel_aspect_ratio_index": to_enum_from_index(PresetPixelAspectRatios),
            "clean_width": int,
            "clean_height": int,
            "left_offset": int,
            "top_offset": int,
            "signal_range_index": to_enum_from_index(PresetSignalRanges),
            "color_spec_index": to_enum_from_index(PresetColorSpecs),
        },
    )
)
"""
(B) Base video format specifications from (Table B.1a, B.1b, B.1c), indexed by
:py:class:`~.BaseVideoFormats`.
"""

################################################################################
# (15.4.4) Lifting filters
################################################################################


class LiftingFilterTypes(IntEnum):
    """
    (15.4.4.1) Indices of lifting filter step types. Names are informative and
    based on an interpretation of the pseudo-code in the specification.
    """
    even_add_odd = 1
    even_subtract_odd = 2
    odd_add_even = 3
    odd_subtract_even = 4


class WaveletFilters(IntEnum):
    """
    (12.4.2) Wavelet filter types supported by VC-2 using the indices
    normitively specified in  in (Table 12.1). Names are based on the
    informative names in the table.
    
    See also: :py:data:`~.tables.LIFTING_FILTERS`.
    """
    
    deslauriers_dubuc_9_7 = 0
    le_gall_5_3 = 1
    deslauriers_dubuc_13_7 = 2
    haar_no_shift = 3
    haar_with_shift = 4
    fidelity = 5
    daubechies_9_7 = 6


LiftingStage = namedtuple("LiftingStage", "lift_type,S,L,D,taps")
"""
(15.4.4.1) Definition of a lifting stage/operation in a lifting filter.

Parameters
----------
lift_type
    Specifies which lifting filtering operation is taking place. One
    of the indices from the LiftingFilterTypes enumeration.
S
    Scale factor (right-shift applied to weighted sum)
L
    Length of filter.
D
    Offset of filter.
taps
    An array of integers defining the filter coefficients.
"""

LiftingFilterParameters = namedtuple("LiftingFilterParameters", "filter_bit_shift,stages")
"""
(15.4.4.3) The generic container for the details described by (Table 15.1
to 15.6).

Parameters
----------
filter_bit_shift
    Right-shift to apply after synthesis (or before analysis).
stages
    A list of LiftingStage objects to be used in sequence to perform synthesis
    with this filter.
"""

LIFTING_FILTERS = {
    WaveletFilters.deslauriers_dubuc_9_7: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=2, L=2, D=0, taps=[1, 1]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=4, L=4, D=-1, taps=[-1, 9, 9, -1]),
        ],
        filter_bit_shift=1,
    ),
    WaveletFilters.le_gall_5_3: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=2, L=2, D=0, taps=[1, 1]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=1, L=2, D=0, taps=[1, 1]),
        ],
        filter_bit_shift=1,
    ),
    WaveletFilters.deslauriers_dubuc_13_7: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=5, L=4, D=-1, taps=[-1, 9, 9, -1]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=4, L=4, D=-1, taps=[-1, 9, 9, -1]),
        ],
        filter_bit_shift=1,
    ),
    WaveletFilters.haar_no_shift: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=1, L=1, D=1, taps=[1]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=0, L=1, D=0, taps=[1]),
        ],
        filter_bit_shift=0,
    ),
    WaveletFilters.haar_with_shift: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=1, L=1, D=1, taps=[1]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=0, L=1, D=0, taps=[1]),
        ],
        filter_bit_shift=1,
    ),
    WaveletFilters.fidelity: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(3), S=8, L=8, D=-3, taps=[-2, -10, -25, 81, 81, -25, 10, -2]),
            LiftingStage(lift_type=LiftingFilterTypes(2), S=8, L=8, D=-3, taps=[-8, 21, -46, 161, 161, -46, 21, -8]),
        ],
        filter_bit_shift=0,
    ),
    WaveletFilters.daubechies_9_7: LiftingFilterParameters(
        stages=[
            LiftingStage(lift_type=LiftingFilterTypes(2), S=12, L=2, D=0, taps=[1817, 1817]),
            LiftingStage(lift_type=LiftingFilterTypes(4), S=12, L=2, D=0, taps=[3616, 3616]),
            LiftingStage(lift_type=LiftingFilterTypes(1), S=12, L=2, D=0, taps=[217, 217]),
            LiftingStage(lift_type=LiftingFilterTypes(3), S=12, L=2, D=0, taps=[6497, 6497]),
        ],
        filter_bit_shift=1,
    ),
}
"""
(15.4.4.3) Filter definitions taken from (Table 15.1 to 15.6) indexed by :py:class:`~.constants.WaveletFilters`.
"""

################################################################################
# (C.2) Profiles
################################################################################

Profiles = read_enum_from_csv("profiles.csv", "Profiles")
"""(C.2) VC-2 profile identifiers."""

ProfileParameters = namedtuple("ProfileParameters", "allowed_parse_codes, ")
"""
(C.2) Parameters describing a profile specification.

Parameters
----------
allowed_parse_codes
    A list of supported data units. A list of values from the ParseCodes enum.
"""

PROFILES = (
    read_lookup_from_csv(
        "profiles.csv",
        Profiles,
        ProfileParameters,
        type_conversions={
            "allowed_parse_codes": to_list(to_enum_from_name(ParseCodes)),
        }
    )
)
"""
The list of supported profiles from (C.2) indexed by :py:class:`~.Profiles`.
"""

################################################################################
# (D) Quantisation matrices
################################################################################

QUANTISATION_MATRICES = read_quantisation_matrices_from_csv("quantisation_matrices.csv")
"""
The preset quantisation matrices from (Table D.1) to (Table D.8)

The loaded matrices are stored in a nested dictionary with the following
layout::

    QUANTISATION_MATRICES[(wavelet_index, wavelet_index_ho, dwt_depth, dwt_depth_ho)][level][orientation]

Where:

* ``wavelet_index`` and ``wavelet_index_ho`` are :py:class:`WaveletFilters`
  values
* ``dwt_depth`` and ``dwt_depth_ho`` are transform depths (integers)
* ``level`` is the transform level (integer)
* ``orientation`` is one of `"L"`, `"H"`, `"LL"``, `"HL"``, `"LH"`` or `"HH"``
"""

################################################################################
# (ST 2042-2) Levels
################################################################################

Levels = read_enum_from_csv("levels.csv", "Levels")
"""(ST 2042-2:2017: 5.2) VC-2 level identifiers."""

LevelParameters = namedtuple(
    "LevelParameters",
    (
        "standard,"
        "sequence_restriction_explanation,"
        "sequence_restriction_regex,"
    ),
)
"""
(ST 2042-2) Parameters describing a level.

Parameters
----------
standard : str
    Name of the standards document which defines the level.
sequence_restriction_explanation : str
    Human readable explanation of the allowed ordering of data units in
    sequences for printing in error messages.
sequence_restriction_regex : str
    A :py:mod:`vc2_conformance._symbol_re` regular expression describing the
    allowed sequencing of data units in a sequence while using this level.
"""

LEVELS = (
    read_lookup_from_csv("levels.csv", Levels, LevelParameters)
)
"""
The list of supported levels from (ST 2042-2:2017: 5.2) indexed by
:py:class:`~.Levels`.
"""
