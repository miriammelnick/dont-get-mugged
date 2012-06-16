
###############################################################################
#
# UpdateActiveSubscription
# Subscribes a customer to a specified plan.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateActiveSubscription(Choreography):

    """
    Create a new instance of the UpdateActiveSubscription Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/UpdateActiveSubscription')


    def new_input_set(self):
        return UpdateActiveSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return UpdateActiveSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateActiveSubscriptionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateActiveSubscription
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateActiveSubscriptionInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the AddressLine1 input for this choreography. ((optional, string) The first line of the address that is associated with the credit card billing address)
        """
        def set_AddressLine1(self, value):
            InputSet._set_input(self, 'AddressLine1', value)

        """
        Set the value of the AddressLine2 input for this choreography. ((optional, string) The second line of the address that is associated with the credit card billing address)
        """
        def set_AddressLine2(self, value):
            InputSet._set_input(self, 'AddressLine2', value)

        """
        Set the value of the CVC input for this choreography. ((optional, integer) The 3-digit card security code)
        """
        def set_CVC(self, value):
            InputSet._set_input(self, 'CVC', value)

        """
        Set the value of the CardNumber input for this choreography. ((optional, integer) The credit card number without any separators. Required when updating credit card details.)
        """
        def set_CardNumber(self, value):
            InputSet._set_input(self, 'CardNumber', value)

        """
        Set the value of the CardholderName input for this choreography. ((optional, string) The cardholder's full name as it appears on the credit card)
        """
        def set_CardholderName(self, value):
            InputSet._set_input(self, 'CardholderName', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) The country associated with the credit card billing address)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Coupon input for this choreography. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        def set_Coupon(self, value):
            InputSet._set_input(self, 'Coupon', value)

        """
        Set the value of the CustomerId input for this choreography. ((string) The unique identifier of the customer you want to subscribe to a plan)
        """
        def set_CustomerId(self, value):
            InputSet._set_input(self, 'CustomerId', value)

        """
        Set the value of the ExpirationMonth input for this choreography. ((optional, integer) The card's expiration month as a two digit number. Required when updating credit card details.)
        """
        def set_ExpirationMonth(self, value):
            InputSet._set_input(self, 'ExpirationMonth', value)

        """
        Set the value of the ExpirationYear input for this choreography. ((optional, integer) The card's expiration year as a four digit number. Required when updating credit card details.)
        """
        def set_ExpirationYear(self, value):
            InputSet._set_input(self, 'ExpirationYear', value)

        """
        Set the value of the Plan input for this choreography. ((string) The unique identifier of the plan to subscribe the customer to)
        """
        def set_Plan(self, value):
            InputSet._set_input(self, 'Plan', value)

        """
        Set the value of the Prorate input for this choreography. ((optional, boolean) When set to 1, Stripe will prorate switching plans during a billing cycle. When set to 0, this feature is disabled. Defaults to 1.)
        """
        def set_Prorate(self, value):
            InputSet._set_input(self, 'Prorate', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state of the address that is associated with the credit card billing address)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Token input for this choreography. ((optional, string) The token associated with a set of credit card details. This can be used as an alternative to specifying credit card details.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the TrialEnd input for this choreography. ((optional, date) A timestamp representing the end of the trial period in UTC. The customer will not be charged during the trial period.)
        """
        def set_TrialEnd(self, value):
            InputSet._set_input(self, 'TrialEnd', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The zip code of the address that is associated with the credit card billing address)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateActiveSubscription choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateActiveSubscriptionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateActiveSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateActiveSubscriptionResultSet(response, path)
