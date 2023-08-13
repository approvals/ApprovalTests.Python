'''

TEST_CASE("Test StringTemplates")
{
    // begin-snippet: templated_custom_namer_example
    ApprovalTests::TemplatedCustomNamer namer(
        "/my/source/directory/{ApprovedOrReceived}/"
        "{TestFileName}.{TestCaseName}.{FileExtension}");
    // end-snippet

    CHECK(namer.getApprovedFileAsPath(".txt").toString("/") ==
          "/my/source/directory/approved/"
          "TemplatedCustomNamerExamples.Test_StringTemplates.txt");
    CHECK(namer.getReceivedFileAsPath(".txt").toString("/") ==
          "/my/source/directory/received/"
          "TemplatedCustomNamerExamples.Test_StringTemplates.txt");
}
'''
from typing import Optional

from approvaltests import get_default_namer, verify, Namer


class TemplatedCustomNamer(Namer):
    def __init__(self, template: str):
        self.template = template
    def get_received_filename(self, base: Optional[str] = None) -> str:
        #build up this string and return it
        #/my/source/directory/received/test_templated_namer.test_string_templates.txt
        # return "/my/source/directory/received/test_templated_namer.test_string_templates.txt"
        return self.template.format(ApprovedOrReceived="received",TestFileName="test_templated_namer")

    def get_approved_filename(self, base: Optional[str] = None) -> str:
        pass


def test_string_templates():
    namer = TemplatedCustomNamer( "/my/source/directory/{ApprovedOrReceived}/{TestFileName}.{TestCaseName}.{FileExtension}")
    assert(namer.get_received_filename() == "/my/source/directory/received/"
          "test_templated_namer.test_string_templates.txt")



