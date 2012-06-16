
###############################################################################
#
# DeleteTag
# Removes a tag from a specified photo in Google Picasa.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteTag(Choreography):

    """
    Create a new instance of the DeleteTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/DeleteTag')


    def new_input_set(self):
        return DeleteTagInputSet()

    def _make_result_set(self, result, path):
        return DeleteTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteTagInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the AlbumId input for this choreography. ((integer) The id for the album which has the tagged photo. Note that this can be retrieved by running the ListAlbums Choreo.)
        """
        def set_AlbumId(self, value):
            InputSet._set_input(self, 'AlbumId', value)

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
        Set the value of the PhotoId input for this choreography. ((integer) The Id for the photo that has a tag to delete)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the Oauth process to be used when your access token expires)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the TagId input for this choreography. ((string) The Id (or tag name) for the tag that you want to delete)
        """
        def set_TagId(self, value):
            InputSet._set_input(self, 'TagId', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteTagResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google Picasa)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class DeleteTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTagResultSet(response, path)