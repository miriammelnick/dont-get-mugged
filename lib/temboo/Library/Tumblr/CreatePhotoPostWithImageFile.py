
###############################################################################
#
# CreatePhotoPostWithImageFile
# Creates a new photo post using a an image that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreatePhotoPostWithImageFile(Choreography):

    """
    Create a new instance of the CreatePhotoPostWithImageFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/CreatePhotoPostWithImageFile')


    def new_input_set(self):
        return CreatePhotoPostWithImageFileInputSet()

    def _make_result_set(self, result, path):
        return CreatePhotoPostWithImageFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePhotoPostWithImageFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreatePhotoPostWithImageFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreatePhotoPostWithImageFileInputSet(InputSet):
        """
        Set the value of the Data input for this choreography. ((conditional, string) The base64 ecoded contents of the image you want to post. Required unless you using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_Data(self, value):
            InputSet._set_input(self, 'Data', value)

        """
        Set the value of the BaseHostname input for this choreography. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com))
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the Caption input for this choreography. ((optional, string) The user-supplied caption. HTML is allowed.)
        """
        def set_Caption(self, value):
            InputSet._set_input(self, 'Caption', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Link input for this choreography. ((optional, string) The "click-through URL" for the photo)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the Markdown input for this choreography. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        def set_Markdown(self, value):
            InputSet._set_input(self, 'Markdown', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Tumblr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Tumblr after registering your application)
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
        Set the value of the Slug input for this choreography. ((optional, string) Adds a short text summary to the end of the post URL)
        """
        def set_Slug(self, value):
            InputSet._set_input(self, 'Slug', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) Comma-separated tags for this post)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the Tweet input for this choreography. ((optional, string) Manages the autotweet (if enabled) for this post. Defaults to off for no tweet. Enter text to override the default tweet.)
        """
        def set_Tweet(self, value):
            InputSet._set_input(self, 'Tweet', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A path to an image in the vault that you want to post. Required unless specifying the image contents in the Data input.)
        """


"""
A ResultSet with methods tailored to the values returned by the CreatePhotoPostWithImageFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreatePhotoPostWithImageFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreatePhotoPostWithImageFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreatePhotoPostWithImageFileResultSet(response, path)
