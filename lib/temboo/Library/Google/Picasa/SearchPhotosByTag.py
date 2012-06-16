
###############################################################################
#
# SearchPhotosByTag
# Searches photos using tags that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchPhotosByTag(Choreography):

    """
    Create a new instance of the SearchPhotosByTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/SearchPhotosByTag')


    def new_input_set(self):
        return SearchPhotosByTagInputSet()

    def _make_result_set(self, result, path):
        return SearchPhotosByTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchPhotosByTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchPhotosByTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchPhotosByTagInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the Oauth process)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientId input for this choreography. ((string) The client id provided by Google Pacasa when you sign up for an account)
        """
        def set_ClientId(self, value):
            InputSet._set_input(self, 'ClientId', value)

        """
        Set the value of the ClientSecret input for this choreography. ((string) The client secret provided by Google Picasa when you sign up for an account)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the Oauth process to be used when your access token expires)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the Tag input for this choreography. ((string) A photo tag to search by. Multiple tags can be separated by commas.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the SearchPhotosByTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchPhotosByTagResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((string) The access token retrieved in the last step of the Oauth process)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class SearchPhotosByTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchPhotosByTagResultSet(response, path)
