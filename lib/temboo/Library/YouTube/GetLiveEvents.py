
###############################################################################
#
# GetLiveEvents
# Retrieve a list of live video events.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLiveEvents(Choreography):

    """
    Create a new instance of the GetLiveEvents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/YouTube/GetLiveEvents')


    def new_input_set(self):
        return GetLiveEventsInputSet()

    def _make_result_set(self, result, path):
        return GetLiveEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLiveEventsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLiveEvents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLiveEventsInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Specify the maximum number of results to return. The default value is 10, the maximum value is 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) Specify the first matching result to return. Uses a one-based index (the first result is 1 by default).)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the Type input for this choreography. ((string) Specify the kind of live YouTube event list to retrieve: featured, live_now, upcoming, or recently_broadcasted.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the GetLiveEvents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLiveEventsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The result set returned by the API call.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLiveEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLiveEventsResultSet(response, path)
