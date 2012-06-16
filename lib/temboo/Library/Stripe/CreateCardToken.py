
###############################################################################
#
# CreateCardToken
# Creates a single use token associated with credit card details.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateCardToken(Choreography):

    """
    Create a new instance of the CreateCardToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CreateCardToken')


    def new_input_set(self):
        return CreateCardTokenInputSet()

    def _make_result_set(self, result, path):
        return CreateCardTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCardTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateCardToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateCardTokenInputSet(InputSet):
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
        Set the value of the Amount input for this choreography. ((optional, integer) The amount to charge a customer in cents. This option will guarantee that there are enough funds to satisfy a charge for this amount. )
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the CVC input for this choreography. ((optional, integer) The 3-digit card security code )
        """
        def set_CVC(self, value):
            InputSet._set_input(self, 'CVC', value)

        """
        Set the value of the CardNumber input for this choreography. ((integer) The credit card number without any separators)
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
        Set the value of the Currency input for this choreography. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        def set_Currency(self, value):
            InputSet._set_input(self, 'Currency', value)

        """
        Set the value of the ExpirationMonth input for this choreography. ((integer) The card's expiration month as a two digit number)
        """
        def set_ExpirationMonth(self, value):
            InputSet._set_input(self, 'ExpirationMonth', value)

        """
        Set the value of the ExpirationYear input for this choreography. ((integer) The card's expiration year as a 4 digit number)
        """
        def set_ExpirationYear(self, value):
            InputSet._set_input(self, 'ExpirationYear', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state of the address that is associated with the credit card billing address)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The zip code of the address that is associated with the credit card billing address)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the CreateCardToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateCardTokenResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateCardTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCardTokenResultSet(response, path)
