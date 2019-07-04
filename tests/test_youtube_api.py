from simple_youtube_api.Comment import Comment
from simple_youtube_api.CommentThread import CommentThread
from simple_youtube_api import youtube_api

import pytest
import os
import json

data_dir = 'test_data'


def test_parse_comment_thread():
    data_path = os.path.dirname(os.path.abspath(__file__)) + os.sep +\
                                data_dir + os.sep + "comment_thread_test.json"

    with open(data_path, 'r') as f:
        data = json.loads(f.read())

    comment_thread = CommentThread()
    comment_thread = youtube_api.parse_comment_thread(comment_thread, data)

    assert comment_thread.id == data['id']

    # snippet
    snippet_data = data.get('snippet', False)
    if snippet_data:
        assert comment_thread.channel_id == snippet_data.get('channelId', None)
        assert comment_thread.video_id == snippet_data.get('videoId', None)
        assert comment_thread.can_reply == snippet_data['canReply']
        assert comment_thread.total_reply_count ==\
            snippet_data['totalReplyCount']
        assert comment_thread.is_public == snippet_data['isPublic']


def test_parse_comment():
    data_path = os.path.dirname(os.path.abspath(__file__)) + os.sep +\
                                data_dir + os.sep + "comment_test.json"

    with open(data_path, 'r') as f:
        data = json.loads(f.read())

    comment = Comment()
    comment = youtube_api.parse_comment(comment, data)

    assert comment.etag == data['etag']
    assert comment.id == data['id']

    # snippet
    snippet_data = data.get('snippet', False)
    if snippet_data:
        assert comment.author_display_name == snippet_data['authorDisplayName']
        assert comment.author_profile_image_url == \
            snippet_data['authorProfileImageUrl']
        assert comment.author_channel_url == snippet_data['authorChannelUrl']
        assert comment.author_channel_id == \
            snippet_data['authorChannelId']['value']
        assert comment.channel_id == snippet_data.get('videoId', None)
        assert comment.video_id == snippet_data.get('videoId', None)
        assert comment.text_display == snippet_data['textDisplay']
        assert comment.text_original == snippet_data['textOriginal']
        assert comment.parent_id == snippet_data.get('parentId', None)
        assert comment.can_rate == snippet_data['canRate']
        assert comment.viewer_rating == snippet_data['viewerRating']
        assert comment.like_counter == snippet_data['likeCount']
        assert comment.moderation_status == snippet_data.get('moderationStatus', None)
        assert comment.published_at == snippet_data['publishedAt']
        assert comment.updated_at == snippet_data['updatedAt']


if __name__ == "__main__":
    pytest.main()
