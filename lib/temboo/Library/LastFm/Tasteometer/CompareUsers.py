
###############################################################################
#
# CompareUsers
# Retrieves a Tasteometer score from two user inputs, along with a list of shared artists.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CompareUsers(Choreography):

    """
    Create a new instance of the CompareUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Tasteometer/CompareUsers')


    def new_input_set(self):
        return CompareUsersInputSet()

    def _make_result_set(self, result, path):
        return CompareUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CompareUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CompareUsersInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) How many shared artists to display. Defaults to 5.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the User1 input for this choreography. ((string) The first user to compare.)
        """
        def set_User1(self, value):
            InputSet._set_input(self, 'User1', value)

        """
        Set the value of the User2 input for this choreography. ((string) The second user to compare.)
        """
        def set_User2(self, value):
            InputSet._set_input(self, 'User2', value)


"""
A ResultSet with methods tailored to the values returned by the CompareUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CompareUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CompareUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompareUsersResultSet(response, path)
