
###############################################################################
#
# AddTags
# Add a tag to a specified photo on Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddTags(Choreography):

    """
    Create a new instance of the AddTags Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoComments/AddTags')


    def new_input_set(self):
        return AddTagsInputSet()

    def _make_result_set(self, result, path):
        return AddTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTagsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddTags
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddTagsInputSet(InputSet):
        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Flickr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Flickr after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the PhotoId input for this choreography. ((integer) The id of the photo to add tags to)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)

        """
        Set the value of the Tags input for this choreography. ((string) The tags to add to the photo. Multiple tags can be separated by spaces.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)


"""
A ResultSet with methods tailored to the values returned by the AddTags choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddTagsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Flickr)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddTagsResultSet(response, path)
