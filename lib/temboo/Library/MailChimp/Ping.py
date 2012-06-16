
###############################################################################
#
# Ping
# Test connection to MailChimp services.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Ping(Choreography):

    """
    Create a new instance of the Ping Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Ping')


    def new_input_set(self):
        return PingInputSet()

    def _make_result_set(self, result, path):
        return PingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Ping
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PingInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)


"""
A ResultSet with methods tailored to the values returned by the Ping choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Mailchimp.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PingResultSet(response, path)
