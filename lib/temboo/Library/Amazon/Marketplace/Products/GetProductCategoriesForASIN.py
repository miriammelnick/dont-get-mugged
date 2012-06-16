
###############################################################################
#
# GetProductCategoriesForASIN
# Returns the product categories that a product belongs to, including parent categories back to the root for the marketplace. This method uses a MarketplaceId and an ASIN to uniquely identify a product.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetProductCategoriesForASIN(Choreography):

    """
    Create a new instance of the GetProductCategoriesForASIN Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Products/GetProductCategoriesForASIN')


    def new_input_set(self):
        return GetProductCategoriesForASINInputSet()

    def _make_result_set(self, result, path):
        return GetProductCategoriesForASINResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetProductCategoriesForASINChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetProductCategoriesForASIN
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetProductCategoriesForASINInputSet(InputSet):
        """
        Set the value of the ASIN input for this choreography. ((required, string) An ASIN value used to identify a product in the given marketplace.)
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
A ResultSet with methods tailored to the values returned by the GetProductCategoriesForASIN choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetProductCategoriesForASINResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetProductCategoriesForASINChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetProductCategoriesForASINResultSet(response, path)
