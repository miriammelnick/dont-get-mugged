
###############################################################################
#
# PostalCodeInquiryRequest
# Retrieves location information from FedEx Web Services for a specified postal code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PostalCodeInquiryRequest(Choreography):

    """
    Create a new instance of the PostalCodeInquiryRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedEx/PostalCodeInquiryRequest')


    def new_input_set(self):
        return PostalCodeInquiryRequestInputSet()

    def _make_result_set(self, result, path):
        return PostalCodeInquiryRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PostalCodeInquiryRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PostalCodeInquiryRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PostalCodeInquiryRequestInputSet(InputSet):
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
        Set the value of the CountryCode input for this choreography. ((required, string) The country code to use in the inquiry request)
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
        Set the value of the PostalCode input for this choreography. ((required, string) The postal code to use in the inquiry request)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)


"""
A ResultSet with methods tailored to the values returned by the PostalCodeInquiryRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PostalCodeInquiryRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedEx)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PostalCodeInquiryRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PostalCodeInquiryRequestResultSet(response, path)
