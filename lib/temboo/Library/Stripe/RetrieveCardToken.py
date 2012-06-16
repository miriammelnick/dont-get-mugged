
###############################################################################
#
# RetrieveCardToken
# Retrieves a card token based on a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveCardToken(Choreography):

    """
    Create a new instance of the RetrieveCardToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/RetrieveCardToken')


    def new_input_set(self):
        return RetrieveCardTokenInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCardTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCardTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveCardToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveCardTokenInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the TokenId input for this choreography. ((string) The unique identifier of the token you want to retrieve)
        """
        def set_TokenId(self, value):
            InputSet._set_input(self, 'TokenId', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveCardToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveCardTokenResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveCardTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCardTokenResultSet(response, path)
