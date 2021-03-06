
###############################################################################
#
# AddressValidationRequest
# Allows you to submit an address for validation to FedEx Web Services.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddressValidationRequest(Choreography):

    """
    Create a new instance of the AddressValidationRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedEx/AddressValidationRequest')


    def new_input_set(self):
        return AddressValidationRequestInputSet()

    def _make_result_set(self, result, path):
        return AddressValidationRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddressValidationRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddressValidationRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddressValidationRequestInputSet(InputSet):
        """
        Set the value of the AccountNumber input for this choreography. ((required, string) Your FedEx Account Number)
        """
        def set_AccountNumber(self, value):
            InputSet._set_input(self, 'AccountNumber', value)

        """
        Set the value of the AuthenticationKey input for this choreography. ((required, string) The Production Authentication Key provided by FedEx Web Services)
        """
        def set_AuthenticationKey(self, value):
            InputSet._set_input(self, 'AuthenticationKey', value)

        """
        Set the value of the City input for this choreography. ((required, string) The city to use in the address validation request)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the CountryCode input for this choreography. ((required, string) The country code to use in the address validation request)
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the MeterNumber input for this choreography. ((required, string) The Production Meter Number provided by FedEx Web Services)
        """
        def set_MeterNumber(self, value):
            InputSet._set_input(self, 'MeterNumber', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Production Password provided by FedEx Web Services)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PostalCode input for this choreography. ((required, string) The postal code to use in the address validation request)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)

        """
        Set the value of the State input for this choreography. ((required, string) The state to use in the address validation request)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Street input for this choreography. ((required, string) The street to use in the address validation request)
        """
        def set_Street(self, value):
            InputSet._set_input(self, 'Street', value)


"""
A ResultSet with methods tailored to the values returned by the AddressValidationRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddressValidationRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedEx)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "DeliveryPointValidation" output from this choreography execution. ((string) The Delivery Point Validation parsed from the FedEx response)
        """
        def get_DeliveryPointValidation(self):
            return self._output.get('DeliveryPointValidation', None)

class AddressValidationRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddressValidationRequestResultSet(response, path)
