
###############################################################################
#
# CreateAlbum
# Creates a photo album in a Google Picasa account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAlbum(Choreography):

    """
    Create a new instance of the CreateAlbum Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/CreateAlbum')


    def new_input_set(self):
        return CreateAlbumInputSet()

    def _make_result_set(self, result, path):
        return CreateAlbumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAlbumChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAlbum
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAlbumInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
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
        Set the value of the Keywords input for this choreography. ((optional, string) Keywords to associate with the album you are creating separated by commas)
        """
        def set_Keywords(self, value):
            InputSet._set_input(self, 'Keywords', value)

        """
        Set the value of the PhotoAccess input for this choreography. ((optional, string) The perssion level to specify for photo access. Defaults to 'public'.)
        """
        def set_PhotoAccess(self, value):
            InputSet._set_input(self, 'PhotoAccess', value)

        """
        Set the value of the PhotoLocation input for this choreography. ((optional, string) The location to associate with the photo (i.e. Italy))
        """
        def set_PhotoLocation(self, value):
            InputSet._set_input(self, 'PhotoLocation', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the Oauth process to be used when your access token expires)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the Summary input for this choreography. ((optional, string) The album summary)
        """
        def set_Summary(self, value):
            InputSet._set_input(self, 'Summary', value)

        """
        Set the value of the Timestamp input for this choreography. ((optional, date) The timestamp to associate with the photo.  Defaults to the current timestamp. Should be an epoch timestamp in milliseconds.)
        """
        def set_Timestamp(self, value):
            InputSet._set_input(self, 'Timestamp', value)

        """
        Set the value of the Title input for this choreography. ((string) The title of the album)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the CreateAlbum choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAlbumResultSet(ResultSet):
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

class CreateAlbumChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAlbumResultSet(response, path)
