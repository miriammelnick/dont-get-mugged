
###############################################################################
#
# GetMatchingProduct
# Returns a list of products and their attributes, based on a ASIN value that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMatchingProduct(Choreography):

    """
    Create a new instance of the GetMatchingProduct Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Products/GetMatchingProduct')


    def new_input_set(self):
        return GetMatchingProductInputSet()

    def _make_result_set(self, result, path):
        return GetMatchingProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMatchingProductChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMatchingProduct
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMatchingProductInputSet(InputSet):
        """
        Set the value of the ASIN input for this choreography. ((required, string) An ASIN value used to identify products in the given marketplace.)
        """
        def set_ASIN(self, value):
            InputSet._set_input(self, 'ASIN', value)

        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSMarketplaceId input for this choreography. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        def set_AWSMarketplaceId(self, value):
            InputSet._set_input(self, 'AWSMarketplaceId', value)

        """
        Set the value of the AWSMerchantId input for this choreography. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        def set_AWSMerchantId(self, value):
            InputSet._set_input(self, 'AWSMerchantId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)


"""
A ResultSet with methods tailored to the values returned by the GetMatchingProduct choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMatchingProductResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMatchingProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMatchingProductResultSet(response, path)
