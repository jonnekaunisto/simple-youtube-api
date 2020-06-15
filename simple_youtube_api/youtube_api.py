import argparse
import time
import random
import http.client
import httplib2
import pickle
import os

from simple_youtube_api.youtube_constants import *

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage


# autogenerate code, do not edit
def parse_youtube_video(video, data):
    video.etag = data["etag"]
    video.id = data["id"]

    # snippet
    snippet_data = data.get("snippet", False)
    if snippet_data:
        video.published_at = snippet_data.get("publishedAt", None)
        video.channel_id = snippet_data.get("channelId", None)
        video.title = snippet_data.get("title", None)
        video.description = snippet_data.get("description", None)
        video.channel_title = snippet_data.get("channelTitle", None)
        video.tags = snippet_data.get("tags", None)
        video.category_id = snippet_data.get("categoryId", None)
        video.live_broadcast_content = snippet_data.get(
            "liveBroadcastContent", None
        )
        video.default_language = snippet_data.get("defaultLanguage", None)
        video.default_audio_language = snippet_data.get(
            "defaultAudioLanguage", None
        )

    # contentDetails
    content_details_data = data.get("contentDetails", False)
    if content_details_data:
        video.duration = content_details_data.get("duration", None)
        video.dimension = content_details_data.get("dimension", None)
        video.definition = content_details_data.get("definition", None)
        video.caption = content_details_data.get("caption", None)
        video.licensed_content = content_details_data.get(
            "licensedContent", None
        )
        video.projection = content_details_data.get("projection", None)
        video.has_custom_thumbnail = content_details_data.get(
            "hasCustomThumbnail", None
        )

    # status
    status_data = data.get("status", False)
    if status_data:
        video.upload_status = status_data.get("uploadStatus", None)
        video.failure_reason = status_data.get("failureReason", None)
        video.rejection_reason = status_data.get("rejectionReason", None)
        video.privacy_status = status_data.get("privacyStatus", None)
        video.publish_at = status_data.get("publishAt", None)
        video.license = status_data.get("license", None)
        video.embeddable = status_data.get("embeddable", None)
        video.public_stats_viewable = status_data.get(
            "publicStatsViewable", None
        )

    # statistics
    statistics_data = data.get("statistics", False)
    if statistics_data:
        video.view_count = statistics_data.get("viewCount", None)
        video.like_count = statistics_data.get("likeCount", None)
        video.dislike_count = statistics_data.get("dislikeCount", None)
        video.favorite_count = statistics_data.get("favoriteCount", None)
        video.comment_count = statistics_data.get("commentCount", None)

    # player
    player_data = data.get("player", False)
    if player_data:
        video.embed_html = player_data.get("embedHtml", None)
        video.embed_height = player_data.get("embedHeight", None)
        video.embed_width = player_data.get("embedWidth", None)

    # topicDetails
    topic_details_data = data.get("topicDetails", False)
    if topic_details_data:
        video.topic_ids = topic_details_data.get("topicIds", None)
        video.relevant_topic_ids = topic_details_data.get(
            "relevantTopicIds", None
        )
        video.topic_categories = topic_details_data.get("topicCategories", None)

    # recordingDetails
    recording_details_data = data.get("recordingDetails", False)
    if recording_details_data:
        video.recording_date = recording_details_data.get("recordingDate", None)

    # fileDetails
    file_details_data = data.get("fileDetails", False)
    if file_details_data:
        video.file_name = file_details_data.get("fileName", None)
        video.file_size = file_details_data.get("fileSize", None)
        video.file_type = file_details_data.get("fileType", None)
        video.container = file_details_data.get("container", None)
        video.video_streams = file_details_data.get("videoStreams", None)
        video.audio_streams = file_details_data.get("audioStreams", None)
        video.duration_ms = file_details_data.get("durationMs", None)
        video.bitrate_bps = file_details_data.get("bitrateBps", None)
        video.creation_time = file_details_data.get("creationTime", None)

    # processingDetails
    processing_details_data = data.get("processingDetails", False)
    if processing_details_data:
        video.processing_status = processing_details_data.get(
            "processingStatus", None
        )
        video.processing_failure_reason = processing_details_data.get(
            "processingFailureReason", None
        )
        video.file_details_availability = processing_details_data.get(
            "fileDetailsAvailability", None
        )
        video.processing_issues_availability = processing_details_data.get(
            "processingIssuesAvailability", None
        )
        video.tag_suggestions_availability = processing_details_data.get(
            "tagSuggestionsAvailability", None
        )
        video.editor_suggestions_availability = processing_details_data.get(
            "editorSuggestionsAvailability", None
        )
        video.thumbnails_availability = processing_details_data.get(
            "thumbnailsAvailability", None
        )

    # suggestions
    suggestions_data = data.get("suggestions", False)
    if suggestions_data:
        video.processing_errors = suggestions_data.get("processingErrors", None)
        video.processing_warnings = suggestions_data.get(
            "processingWarnings", None
        )
        video.processing_hints = suggestions_data.get("processingHints", None)
        video.tag_suggestions = suggestions_data.get("tagSuggestions", None)
        video.editor_suggestions = suggestions_data.get(
            "editorSuggestions", None
        )

    # liveStreamingDetails
    live_streaming_details_data = data.get("liveStreamingDetails", False)
    if live_streaming_details_data:
        video.actual_start_time = live_streaming_details_data.get(
            "actualStartTime", None
        )
        video.actual_end_time = live_streaming_details_data.get(
            "actualEndTime", None
        )
        video.scheduled_start_time = live_streaming_details_data.get(
            "scheduledStartTime", None
        )
        video.scheduled_end_time = live_streaming_details_data.get(
            "scheduledEndTime", None
        )
        video.concurrent_viewers = live_streaming_details_data.get(
            "concurrentViewers", None
        )
        video.active_live_chat_id = live_streaming_details_data.get(
            "activeLiveChatId", None
        )
    video.localizations = data.get("localizations", None)

    return video


def init_categories(data):
    with open(DATA_PATH + "categories.pickle", "rb") as handle:
        return pickle.load(handle)


def parse_categories(data):
    categories = {}
    for item in data["items"]:
        if item["snippet"]["assignable"]:
            category_name = item["snippet"]["title"]
            category_id = item["id"]
            categories[category_name.lower()] = category_id

    path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "data"
    with open(path + os.sep + "categories.pickle", "wb") as handle:
        pickle.dump(categories, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return categories
