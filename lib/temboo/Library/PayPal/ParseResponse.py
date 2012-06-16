
###############################################################################
#
# ParseResponse
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ParseResponse(Choreography):

    """
    Create a new instance of the ParseResponse Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/ParseResponse')


    def new_input_set(self):
        return ParseResponseInputSet()

    def _make_result_set(self, result, path):
        return ParseResponseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ParseResponseChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ParseResponse
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ParseResponseInputSet(InputSet):
        """
        Set the value of the Response input for this choreography. ((required, string) The response from PayPal in name/value pair format.)
        """
        def set_Response(self, value):
            InputSet._set_input(self, 'Response', value)


"""
A ResultSet with methods tailored to the values returned by the ParseResponse choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ParseResponseResultSet(ResultSet):
        """
        Retrieve the value for the "AssignedKeys" output from this choreography execution. ()
        """
        def get_AssignedKeys(self):
            return self._output.get('AssignedKeys', None)

class ParseResponseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ParseResponseResultSet(response, path)
