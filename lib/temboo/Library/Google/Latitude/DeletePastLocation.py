
###############################################################################
#
# DeletePastLocation
# Deletes a specific location from a user's location history.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeletePastLocation(Choreography):

    """
    Create a new instance of the DeletePastLocation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Latitude/DeletePastLocation')


    def new_input_set(self):
        return DeletePastLocationInputSet()

    def _make_result_set(self, result, path):
        return DeletePastLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePastLocationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeletePastLocation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeletePastLocationInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((string) The client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((string) The client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the LocationID input for this choreography. ((date) Enter the timestamp (in epoch time) of the location to be deleted.)
        """
        def set_LocationID(self, value):
            InputSet._set_input(self, 'LocationID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeletePastLocation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeletePastLocationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeletePastLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePastLocationResultSet(response, path)
