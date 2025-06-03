import pytest
from forensics.usb_parser import parse_usb_logs

def test_usb_parser_valid(tmp_path):
    f = tmp_path / "usb.log"
    f.write_text("usb 1-1: new device found\nusb 1-2: device disconnected")
    assert len(parse_usb_logs(str(f))) == 2

def test_usb_parser_file_not_found():
    with pytest.raises(RuntimeError):
        parse_usb_logs("nonexistent.log")
