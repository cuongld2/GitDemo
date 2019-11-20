import cv2


class TestPlayableVideo:

    def test_playable_mp4(self):
        vid = cv2.VideoCapture('C:\\Users\\cuongld\\Downloads' + '\\' + "video.mp4")
        print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        assert vid.isOpened()

    def test_none_in_text(self):
        assert str(int('')) in 'text'


