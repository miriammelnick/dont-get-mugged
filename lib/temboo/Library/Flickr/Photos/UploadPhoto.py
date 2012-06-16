
###############################################################################
#
# UploadPhoto
# Uploads a photo to Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadPhoto(Choreography):

    """
    Create a new instance of the UploadPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/UploadPhoto')


    def new_input_set(self):
        return UploadPhotoInputSet()

    def _make_result_set(self, result, path):
        return UploadPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadPhotoInputSet(InputSet):
        """
        Set the value of the ImageFileContents input for this choreography. ((conditional, string) The base-64 encoded file contents to upload. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_ImageFileContents(self, value):
            InputSet._set_input(self, 'ImageFileContents', value)

        """
        Set the value of the ContentType input for this choreography. ((optional, integer) The type of content you are uploading. Set to 1 for Photo, 2 for Screenshot, or 3 for Other. Defaults to 1.)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) A description for the photo)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Hidden input for this choreography. ((optional, integer) Set to 1 to allow photos to appear in global search results, 2 to be hidden from public searches. Defaults to 2.)
        """
        def set_Hidden(self, value):
            InputSet._set_input(self, 'Hidden', value)

        """
        Set the value of the IsFamily input for this choreography. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        def set_IsFamily(self, value):
            InputSet._set_input(self, 'IsFamily', value)

        """
        Set the value of the IsFriend input for this choreography. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        def set_IsFriend(self, value):
            InputSet._set_input(self, 'IsFriend', value)

        """
        Set the value of the IsPublic input for this choreography. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        def set_IsPublic(self, value):
            InputSet._set_input(self, 'IsPublic', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Flickr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Flickr after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the SafetyLevel input for this choreography. ((optional, integer) Set value to 1 for Safe, 2 for Moderate, or 3 for Restricted. Defaults to 1.)
        """
        def set_SafetyLevel(self, value):
            InputSet._set_input(self, 'SafetyLevel', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) A list of tags to apply to the photo. Separate multiple tags with spaces.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) The title of the photo you're uploading)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A vault file path can be specified as an alternative to using ImageFileContents input. Required if ImageFileContents is not specified.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadPhotoResultSet(response, path)
