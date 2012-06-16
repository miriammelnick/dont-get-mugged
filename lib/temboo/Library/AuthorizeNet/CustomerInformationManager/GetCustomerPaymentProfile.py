
###############################################################################
#
# GetCustomerPaymentProfile
# Retrieves a payment profile associated with an existing customer profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCustomerPaymentProfile(Choreography):

    """
    Create a new instance of the GetCustomerPaymentProfile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/CustomerInformationManager/GetCustomerPaymentProfile')


    def new_input_set(self):
        return GetCustomerPaymentProfileInputSet()

    def _make_result_set(self, result, path):
        return GetCustomerPaymentProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCustomerPaymentProfileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCustomerPaymentProfile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCustomerPaymentProfileInputSet(InputSet):
        """
        Set the value of the APILoginId input for this choreography. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        def set_APILoginId(self, value):
            InputSet._set_input(self, 'APILoginId', value)

        """
        Set the value of the CustomerPaymentProfileId input for this choreography. ((required, integer) The id for the payment profile you want to retrieve.)
        """
        def set_CustomerPaymentProfileId(self, value):
            InputSet._set_input(self, 'CustomerPaymentProfileId', value)

        """
        Set the value of the CustomerProfileId input for this choreography. ((required, integer) The id of the customer who's payment profile you want to return.)
        """
        def set_CustomerProfileId(self, value):
            InputSet._set_input(self, 'CustomerProfileId', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the TransactionKey input for this choreography. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        def set_TransactionKey(self, value):
            InputSet._set_input(self, 'TransactionKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetCustomerPaymentProfile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCustomerPaymentProfileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Authorize.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCustomerPaymentProfileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCustomerPaymentProfileResultSet(response, path)
