
###############################################################################
#
# ShowUser
# Show Klout data for a specified Twitter user(s).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowUser(Choreography):

    """
    Create a new instance of the ShowUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/ShowUser')


    def new_input_set(self):
        return ShowUserInputSet()

    def _make_result_set(self, result, path):
        return ShowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowUserInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ReturnType input for this choreography. ((optional, string) The desired format for the returned user data: xml or json. Defaults to xml.)
        """
        def set_ReturnType(self, value):
            InputSet._set_input(self, 'ReturnType', value)

        """
        Set the value of the Usernames input for this choreography. ((required, string) A comma-delimited string of Twitter usernames whose Klout data you want to return.)
        """
        def set_Usernames(self, value):
            InputSet._set_input(self, 'Usernames', value)


"""
A ResultSet with methods tailored to the values returned by the ShowUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The retrieved Klout scores for the specified users. The response format depends on what is specified in the ReturnType input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowUserResultSet(response, path)
