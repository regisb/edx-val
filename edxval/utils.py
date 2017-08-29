"""
Util methods to be used in api and models.
"""

from django.conf import settings
from django.core.files.storage import get_storage_class

# 3rd Party Transcription Plans
THIRD_PARTY_TRANSCRIPTION_PLANS = {

    'Cielo24': {
        'display_name': 'Cielo24',
        'turnaround': {
            'PRIORITY': 'Priority (24 hours)',
            'STANDARD': 'Standard (48 hours)'
        },
        'fidelity': {
            'MECHANICAL': {
                'display_name': 'Mechanical (75% Accuracy)',
                'languages': {
                    'nl': 'Dutch',
                    'en': 'English',
                    'fr': 'French',
                    'de': 'German',
                    'it': 'Italian',
                    'es': 'Spanish',
                }
            },
            'PREMIUM': {
                'display_name': 'Premium (95% Accuracy)',
                'languages': {
                    'en': 'English',
                }
            },
            'PROFESSIONAL': {
                'display_name': 'Professional (99% Accuracy)',
                'languages': {
                    'ar': 'Arabic',
                    'zh-tw': 'Chinese - Mandarin (Traditional)',
                    'zh-cmn': 'Chinese - Mandarin (Simplified)',
                    'zh-yue': 'Chinese - Cantonese (Traditional)',
                    'nl': 'Dutch',
                    'en': 'English',
                    'fr': 'French',
                    'de': 'German',
                    'he': 'Hebrew',
                    'hi': 'Hindi',
                    'it': 'Italian',
                    'ja': 'Japanese',
                    'ko': 'Korean',
                    'pt': 'Portuguese',
                    'ru': 'Russian',
                    'es': 'Spanish',
                    'tr': 'Turkish',
                }
            },
        }
    },
    '3PlayMedia': {
        'display_name': '3Play Media',
        'turnaround': {
            'same_day_service': 'Same day',
            'rush_service': '24 hours (rush)',
            'expedited_service': '2 days (expedited)',
            'default': '4 days (default)',
            'extended_service':'10 Days (extended)'
        },
        'languages': {
            'en': 'English',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'nl': 'Dutch',
            'es-419': 'Spanish (Latin America)',
            'pt': 'Portuguese',
            'zh-hans': 'Chinese (Simplified)',
            'zh-cmn-Hant': 'Chinese (Traditional)',
            'ar': 'Arabic',
            'he': 'Hebrew',
            'ru': 'Russian',
            'ja': 'Japanese',
            'sv': 'Swedish',
            'cs': 'Czech',
            'da': 'Danish',
            'fi': 'Finnish',
            'id': 'Indonesian',
            'ko': 'Korean',
            'no': 'Norwegian',
            'pl': 'Polish',
            'th': 'Thai',
            'tr': 'Turkish',
            'vi': 'Vietnamese',
            'ro': 'Romanian',
            'hu': 'Hungarian',
            'ms': 'Malay',
            'bg': 'Bulgarian',
            'tl': 'Tagalog',
            'sr': 'Serbian',
            'sk': 'Slovak',
            'uk': 'Ukrainian',
        }
    }
}


def video_image_path(video_image_instance, filename):  # pylint:disable=unused-argument
    """
    Returns video image path.

    Arguments:
        video_image_instance (VideoImage): This is passed automatically by models.CustomizableImageField
        filename (str): name of image file
    """
    return u'{}{}'.format(settings.VIDEO_IMAGE_SETTINGS.get('DIRECTORY_PREFIX', ''), filename)


def get_video_image_storage():
    """
    Return the configured django storage backend.
    """
    if hasattr(settings, 'VIDEO_IMAGE_SETTINGS'):
        return get_storage_class(
            settings.VIDEO_IMAGE_SETTINGS.get('STORAGE_CLASS'),
        )(**settings.VIDEO_IMAGE_SETTINGS.get('STORAGE_KWARGS', {}))
    else:
        # during edx-platform loading this method gets called but settings are not ready yet
        # so in that case we will return default(FileSystemStorage) storage class instance
        return get_storage_class()()


def video_transcript_path(video_transcript_instance, filename):  # pylint:disable=unused-argument
    """
    Returns video transcript path.

    Arguments:
        video_transcript_instance (VideoTranscript): This is passed automatically by models.CustomizableFileField
        filename (str): name of image file
    """
    return u'{}{}'.format(settings.VIDEO_TRANSCRIPTS_SETTINGS.get('DIRECTORY_PREFIX', ''), filename)


def get_video_transcript_storage():
    """
    Return the configured django storage backend for video transcripts.
    """
    if hasattr(settings, 'VIDEO_TRANSCRIPTS_SETTINGS'):
        return get_storage_class(
            settings.VIDEO_TRANSCRIPTS_SETTINGS.get('STORAGE_CLASS'),
        )(**settings.VIDEO_TRANSCRIPTS_SETTINGS.get('STORAGE_KWARGS', {}))
    else:
        # during edx-platform loading this method gets called but settings are not ready yet
        # so in that case we will return default(FileSystemStorage) storage class instance
        return get_storage_class()()
