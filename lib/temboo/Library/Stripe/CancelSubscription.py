
###############################################################################
#
# CancelSubscription
# Cancels an existing subscription.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CancelSubscription(Choreography):

    """
    Create a new instance of the CancelSubscription Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CancelSubscription')


    def new_input_set(self):
        return CancelSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return CancelSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelSubscriptionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CancelSubscription
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CancelSubscriptionInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the AtPeriodEnd input for this choreography. ((optional, boolean) Delays the cancellation of the subscription until the end of the current period when set to 1. Defaults to 0.)
        """
        def set_AtPeriodEnd(self, value):
            InputSet._set_input(self, 'AtPeriodEnd', value)

        """
        Set the value of the CustomerId input for this choreography. ((string) The id of the customer whose subscription you want to cancel)
        """
        def set_CustomerId(self, value):
            InputSet._set_input(self, 'CustomerId', value)


"""
A ResultSet with methods tailored to the values returned by the CancelSubscription choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CancelSubscriptionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CancelSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelSubscriptionResultSet(response, path)
