
###############################################################################
#
# Available
# Returns the locations that Twitter has trending topic information for.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Available(Choreography):

    """
    Create a new instance of the Available Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Trends/Available')


    def new_input_set(self):
        return AvailableInputSet()

    def _make_result_set(self, result, path):
        return AvailableResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AvailableChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Available
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AvailableInputSet(InputSet):
        """
        Set the value of the Latitude input for this choreography. ((optional, decimal) If provided with a longitude parameter the available trend locations will be sorted by distance, nearest to furthest.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((optional, decimal) If provided with a latitude parameter the available trend locations will be sorted by distance, nearest to furthest.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates what format the response will be in. Acceptable formats are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Available choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AvailableResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Twitter in JSON format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AvailableChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AvailableResultSet(response, path)
