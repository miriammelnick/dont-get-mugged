
###############################################################################
#
# GetWeeklyChartList
# Retrieves a list of available charts for this user, expressed as date ranges which can be sent to the chart services.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWeeklyChartList(Choreography):

    """
    Create a new instance of the GetWeeklyChartList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetWeeklyChartList')


    def new_input_set(self):
        return GetWeeklyChartListInputSet()

    def _make_result_set(self, result, path):
        return GetWeeklyChartListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeeklyChartListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWeeklyChartList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWeeklyChartListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the User input for this choreography. ((string) The last.fm username to fetch the charts of.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetWeeklyChartList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWeeklyChartListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWeeklyChartListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeeklyChartListResultSet(response, path)
