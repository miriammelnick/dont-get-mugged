
###############################################################################
#
# AccountLimits
# Obtain the current rate limit for a Face.com user account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AccountLimits(Choreography):

    """
    Create a new instance of the AccountLimits Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/AccountLimits')


    def new_input_set(self):
        return AccountLimitsInputSet()

    def _make_result_set(self, result, path):
        return AccountLimitsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountLimitsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AccountLimits
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AccountLimitsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your face.com API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Enter your face.com API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml. Defaults to 'xml'.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the AccountLimits choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AccountLimitsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AccountLimitsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountLimitsResultSet(response, path)
