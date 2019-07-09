
def parse_video(video, data):
    video.etag = data['etag']
    video.id = data['id']

    # status
    status_data = data.get('status', False)
    if status_data:
        video.upload_status = status_data['status'].get('uploadStatus', None)
        video.failure_reason = status_data['status'].get('failureReason', None)
        video.rejection_reason = status_data['status'].get('rejectionReason', None)
        video.privacy_status = status_data['status'].get('privacyStatus', None)
        video.publish_at = status_data['status'].get('publishAt', None)
        video.license = status_data['status'].get('license', None)
        video.embeddable = status_data['status'].get('embeddable', None)
        video.public_stats_viewable = status_data['status'].get('publicStatsViewable', None)

    # statistics
    statistics_data = data.get('statistics', False)
    if statistics_data:
        video.view_count = statistics_data['statistics'].get('viewCount', None)
        video.like_count = statistics_data['statistics'].get('likeCount', None)
        video.dislike_count = statistics_data['statistics'].get('dislikeCount', None)
        video.favorite_count = statistics_data['statistics'].get('favoriteCount', None)
        video.comment_count = statistics_data['statistics'].get('commentCount', None)

    # player
    player_data = data.get('player', False)
    if player_data:
        video.embed_html = player_data['player'].get('embedHtml', None)
        video.embed_height = player_data['player'].get('embedHeight', None)
        video.embed_width = player_data['player'].get('embedWidth', None)

    # topicDetails
    topic_details_data = data.get('topicDetails', False)
    if topic_details_data:
        video.topic_ids = topic_details_data['topicDetails'].get('topicIds', None)
        video.relevant_topic_ids = topic_details_data['topicDetails'].get('relevantTopicIds', None)
        video.topic_categories = topic_details_data['topicDetails'].get('topicCategories', None)

    # recordingDetails
    recording_details_data = data.get('recordingDetails', False)
    if recording_details_data:
        video.recording_date = recording_details_data['recordingDetails'].get('recordingDate', None)

    # fileDetails
    file_details_data = data.get('fileDetails', False)
    if file_details_data:
        video.file_name = file_details_data['fileDetails'].get('fileName', None)
        video.file_size = file_details_data['fileDetails'].get('fileSize', None)
        video.file_type = file_details_data['fileDetails'].get('fileType', None)
        video.container = file_details_data['fileDetails'].get('container', None)
        video.video_streams = file_details_data['fileDetails'].get('videoStreams', None)
        video.audio_streams = file_details_data['fileDetails'].get('audioStreams', None)
        video.duration_ms = file_details_data['fileDetails'].get('durationMs', None)
        video.bitrate_bps = file_details_data['fileDetails'].get('bitrateBps', None)
        video.creation_time = file_details_data['fileDetails'].get('creationTime', None)

    # suggestions
    suggestions_data = data.get('suggestions', False)
    if suggestions_data:
        video.processing_errors = suggestions_data['suggestions'].get('processingErrors', None)
        video.processing_warnings = suggestions_data['suggestions'].get('processingWarnings', None)
        video.processing_hints = suggestions_data['suggestions'].get('processingHints', None)
        video.tag_suggestions = suggestions_data['suggestions'].get('tagSuggestions', None)
        video.editor_suggestions = suggestions_data['suggestions'].get('editorSuggestions', None)

    # liveStreamingDetails
    live_streaming_details_data = data.get('liveStreamingDetails', False)
    if live_streaming_details_data:
        video.actual_start_time = live_streaming_details_data['liveStreamingDetails'].get('actualStartTime', None)
        video.actual_end_time = live_streaming_details_data['liveStreamingDetails'].get('actualEndTime', None)
        video.scheduled_start_time = live_streaming_details_data['liveStreamingDetails'].get('scheduledStartTime', None)
        video.scheduled_end_time = live_streaming_details_data['liveStreamingDetails'].get('scheduledEndTime', None)
        video.concurrent_viewers = live_streaming_details_data['liveStreamingDetails'].get('concurrentViewers', None)
        video.active_live_chat_id = live_streaming_details_data['liveStreamingDetails'].get('activeLiveChatId', None)

    return video