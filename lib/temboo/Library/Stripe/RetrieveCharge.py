
###############################################################################
#
# RetrieveCharge
# Retrieves the details of an existing charge.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveCharge(Choreography):

    """
    Create a new instance of the RetrieveCharge Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/RetrieveCharge')


    def new_input_set(self):
        return RetrieveChargeInputSet()

    def _make_result_set(self, result, path):
        return RetrieveChargeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveChargeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveCharge
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveChargeInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the ChargeId input for this choreography. ((optional, string) The unique identifier of the charge you want to retrieve)
        """
        def set_ChargeId(self, value):
            InputSet._set_input(self, 'ChargeId', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveCharge choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveChargeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveChargeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveChargeResultSet(response, path)
