import pytest
from audio_transcriber import transcribe_audio


# Sample parametrization for testing transcription accuracy across different audio formats
#
# TODO: note that we only test the most relevant file formats
#       as this is just a toy project. In a real-world scenario,
#       we would need to test all the supported formats.
@pytest.mark.parametrize(
    "file_path",
    [
        ("tests/samples/test.mp3"),
        ("tests/samples/test.mp4"),
        ("tests/samples/test.mkv"),
    ],
)
def test_audio_transcription(file_path):
    result = transcribe_audio(file_path, model_size="small", language="en")
    result_str = " ".join([segment["text"] for segment in result["segments"]])

    assert (
        result_str
        == " Well, this is important to say and says.  Nothing in life is as important as you think it is while you are thinking about it."
    )
