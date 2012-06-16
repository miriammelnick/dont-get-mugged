
###############################################################################
#
# Daily
# Retrieves the top 20 trending topics for each hour in a given day.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Daily(Choreography):

    """
    Create a new instance of the Daily Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Trends/Daily')


    def new_input_set(self):
        return DailyInputSet()

    def _make_result_set(self, result, path):
        return DailyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DailyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Daily
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DailyInputSet(InputSet):
        """
        Set the value of the Date input for this choreography. ((optional, date) The start date for the report. The date should be formatted YYYY-MM-DD.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Exclude input for this choreography. ((optional, string) Setting this equal to hashtags will remove all hashtags from the trends list.)
        """
        def set_Exclude(self, value):
            InputSet._set_input(self, 'Exclude', value)


"""
A ResultSet with methods tailored to the values returned by the Daily choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DailyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Twitter in JSON format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DailyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DailyResultSet(response, path)
