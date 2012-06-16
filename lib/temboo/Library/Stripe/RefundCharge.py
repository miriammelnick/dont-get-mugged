
###############################################################################
#
# RefundCharge
# Issues a refund of an existing credit card charge.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RefundCharge(Choreography):

    """
    Create a new instance of the RefundCharge Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/RefundCharge')


    def new_input_set(self):
        return RefundChargeInputSet()

    def _make_result_set(self, result, path):
        return RefundChargeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundChargeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RefundCharge
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RefundChargeInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the Amount input for this choreography. ((optional, integer) The amount to refund to the customer in cents. When left empty, the entire charge is refunded.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the ChargeId input for this choreography. ((string) The unique identifier of the charge to be refunded)
        """
        def set_ChargeId(self, value):
            InputSet._set_input(self, 'ChargeId', value)


"""
A ResultSet with methods tailored to the values returned by the RefundCharge choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RefundChargeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RefundChargeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefundChargeResultSet(response, path)
