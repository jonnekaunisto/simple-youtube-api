def parse_comment(comment, data):
    comment.etag = data["etag"]
    comment.id = data["string"]

    # snippet
    snippet_data = data.get("snippet", False)
    if snippet_data:
        comment.author_display_name = author_display_name_data["snippet"][
            "authorDisplayName"
        ]
        comment.author_profile_image_url = author_profile_image_url_data[
            "snippet"
        ]["authorProfileImageUrl"]
        comment.author_channel_url = author_channel_url_data["snippet"][
            "authorChannelUrl"
        ]
        comment.channel_id = channel_id_data["snippet"]["channelId"]
        comment.video_id = video_id_data["snippet"]["videoId"]
        comment.text_display = text_display_data["snippet"]["textDisplay"]
        comment.text_original = text_original_data["snippet"]["textOriginal"]
        comment.parent_id = parent_id_data["snippet"]["parentId"]
        comment.can_rate = can_rate_data["snippet"]["canRate"]
        comment.viewer_rating = viewer_rating_data["snippet"]["viewerRating"]
        comment.like_count = like_count_data["snippet"]["likeCount"]
        comment.moderation_status = moderation_status_data["snippet"][
            "moderationStatus"
        ]
        comment.published_at = published_at_data["snippet"]["publishedAt"]
        comment.updated_at = updated_at_data["snippet"]["updatedAt"]
    return comment
