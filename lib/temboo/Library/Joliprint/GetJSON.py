
###############################################################################
#
# GetJSON
# Retrieves the atributes of a PDF document created from a website URL in JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetJSON(Choreography):

    """
    Create a new instance of the GetJSON Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Joliprint/GetJSON')


    def new_input_set(self):
        return GetJSONInputSet()

    def _make_result_set(self, result, path):
        return GetJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetJSONChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetJSON
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetJSONInputSet(InputSet):
        """
        Set the value of the URL input for this choreography. ((required, string) The URL of the website to convert to a PDF.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetJSON choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetJSONResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response returned by the Joliprint API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetJSONChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetJSONResultSet(response, path)
