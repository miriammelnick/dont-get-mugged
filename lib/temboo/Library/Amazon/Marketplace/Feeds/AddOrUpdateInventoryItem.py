
###############################################################################
#
# AddOrUpdateInventoryItem
# Add or update an individual inventory listing.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddOrUpdateInventoryItem(Choreography):

    """
    Create a new instance of the AddOrUpdateInventoryItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateInventoryItem')


    def new_input_set(self):
        return AddOrUpdateInventoryItemInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateInventoryItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateInventoryItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateInventoryItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddOrUpdateInventoryItemInputSet(InputSet):
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
        Set the value of the ExpeditedShipping input for this choreography. ((optional, string) The expedited shipping options that you offer for this item. Valid values: 3 = UK Only; N = None, no express delivery offered.)
        """
        def set_ExpeditedShipping(self, value):
            InputSet._set_input(self, 'ExpeditedShipping', value)

        """
        Set the value of the FulfillmentCenterId input for this choreography. ((conditional, string) For those merchants using Amazon fulfillment services, this designates which fulfillment network will be used. Required when using Amazon fulfillment services. Valid values are: AMAZON_EU, DEFAULT.)
        """
        def set_FulfillmentCenterId(self, value):
            InputSet._set_input(self, 'FulfillmentCenterId', value)

        """
        Set the value of the ItemCondition input for this choreography. ((conditional, integer) A numerical entry that indicates the condition of the item. Required for new listings. Valid values are: 1-11. See documentation for description of item condition numeric values.)
        """
        def set_ItemCondition(self, value):
            InputSet._set_input(self, 'ItemCondition', value)

        """
        Set the value of the ItemNote input for this choreography. ((optional, string) A description or note for the item you're adding or updating.)
        """
        def set_ItemNote(self, value):
            InputSet._set_input(self, 'ItemNote', value)

        """
        Set the value of the Price input for this choreography. ((conditional, decimal) The price at which the merchant offers the product for sale. Required if ProductId is provided.)
        """
        def set_Price(self, value):
            InputSet._set_input(self, 'Price', value)

        """
        Set the value of the ProductIdType input for this choreography. ((conditional, integer) The type of standard, unique identifier entered in the product-id field. This is a required field if product-id is provided. Valid values are: 1 (ASIN), 2 (ISBN), 3 (UPC), 4  (EAN).)
        """
        def set_ProductIdType(self, value):
            InputSet._set_input(self, 'ProductIdType', value)

        """
        Set the value of the ProductId input for this choreography. ((conditional, string) A standard, alphanumeric string that uniquely identifies the product. This could be a UPC, EAN or ISBN.  This is a required field if product-id-type is provided.)
        """
        def set_ProductId(self, value):
            InputSet._set_input(self, 'ProductId', value)

        """
        Set the value of the Quantity input for this choreography. ((conditional, integer) Enter the quantity of the item you are making available for sale. Required for merchant-fulfilled items. Leave blank for amazon-fullfilled items.)
        """
        def set_Quantity(self, value):
            InputSet._set_input(self, 'Quantity', value)

        """
        Set the value of the SKU input for this choreography. ((required, string) A unique identifier for the product, assigned by the merchant. The SKU must be unique for each product listed.)
        """
        def set_SKU(self, value):
            InputSet._set_input(self, 'SKU', value)

        """
        Set the value of the TimeToWait input for this choreography. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        def set_TimeToWait(self, value):
            InputSet._set_input(self, 'TimeToWait', value)

        """
        Set the value of the WillShipInternationally input for this choreography. ((optional, integer) Specify your international shipping options. Valid values are: 3 = UK Only; 4 = UK and Europe; 5 = UK, Europe, and North America; 6 = Worldwide)
        """
        def set_WillShipInternationally(self, value):
            InputSet._set_input(self, 'WillShipInternationally', value)


"""
A ResultSet with methods tailored to the values returned by the AddOrUpdateInventoryItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddOrUpdateInventoryItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon after submitting the feed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ProcessingStatus" output from this choreography execution. ((string) The processing status of the product submission which is parsed from the Amazon response.)
        """
        def get_ProcessingStatus(self):
            return self._output.get('ProcessingStatus', None)
        """
        Retrieve the value for the "SubmissionId" output from this choreography execution. ((integer) The submission id parsed from the Amazon response.)
        """
        def get_SubmissionId(self):
            return self._output.get('SubmissionId', None)
        """
        Retrieve the value for the "SubmissionResult" output from this choreography execution. ((string) The submission result returned from Amazon.)
        """
        def get_SubmissionResult(self):
            return self._output.get('SubmissionResult', None)

class AddOrUpdateInventoryItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddOrUpdateInventoryItemResultSet(response, path)
