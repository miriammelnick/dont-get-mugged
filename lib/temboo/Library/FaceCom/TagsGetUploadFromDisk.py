
###############################################################################
#
# TagsGetUploadFromDisk
# Display saved tags in photos that have been passed via an uploaded file, or by passing the base64-encoded contents of a photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TagsGetUploadFromDisk(Choreography):

    """
    Create a new instance of the TagsGetUploadFromDisk Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/TagsGetUploadFromDisk')


    def new_input_set(self):
        return TagsGetUploadFromDiskInputSet()

    def _make_result_set(self, result, path):
        return TagsGetUploadFromDiskResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagsGetUploadFromDiskChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TagsGetUploadFromDisk
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TagsGetUploadFromDiskInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((optional, string) The base64 encoded file contents of the image you want to upload. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your Face.com API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Enter your Face.com API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) Enter a javascript method to wrap a JSON-formatted response for JSONP support.  This call is ignored if ResponseFormat=xml)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file you are transferring to Face.com)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the Filter input for this choreography. ((optional, string) Filter results using the following format and options: gender:male/female. For additional options see Choreo documentation.)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Enter the maximum number of tags to be returned. Default: 5.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Namespace input for this choreography. ((optional, string) Enter a default user namespace to be used for all users specified in teh short-hand syntax (user ID, without '@namespace').)
        """
        def set_Namespace(self, value):
            InputSet._set_input(self, 'Namespace', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) Enter: recent, or random.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the PIDs input for this choreography. ((optional, string) Enter photo IDs to retrieve tags from.)
        """
        def set_PIDs(self, value):
            InputSet._set_input(self, 'PIDs', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml.  Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Together input for this choreography. ((optional, string) If specifying multiple UIDs, return only those photos where ALL UIDs appear together in the photo. Default: false.)
        """
        def set_Together(self, value):
            InputSet._set_input(self, 'Together', value)

        """
        Set the value of the UIDs input for this choreography. ((optional, string) Enter a comma-separated list of user IDs to retrieve.)
        """
        def set_UIDs(self, value):
            InputSet._set_input(self, 'UIDs', value)

        """
        Set the value of the UserAuth input for this choreography. ((optional, string) Use to access Facebook and Twitter resources for tagging.  Enter name:value pairs, comma-separated. EXAMPLE fb_user:[facebook user_id].)
        """
        def set_UserAuth(self, value):
            InputSet._set_input(self, 'UserAuth', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to a file in the vault. Can be used as an alternative to the FileContents input. It is required if FileContents is not used.)
        """


"""
A ResultSet with methods tailored to the values returned by the TagsGetUploadFromDisk choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TagsGetUploadFromDiskResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TagsGetUploadFromDiskChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TagsGetUploadFromDiskResultSet(response, path)
