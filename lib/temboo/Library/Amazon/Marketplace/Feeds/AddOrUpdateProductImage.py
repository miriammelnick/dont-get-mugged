
###############################################################################
#
# AddOrUpdateProductImage
# Adds or updates a product image with a given image location and SKU.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddOrUpdateProductImage(Choreography):

    """
    Create a new instance of the AddOrUpdateProductImage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateProductImage')


    def new_input_set(self):
        return AddOrUpdateProductImageInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateProductImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateProductImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateProductImage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddOrUpdateProductImageInputSet(InputSet):
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
        Set the value of the ImageLocation input for this choreography. ((required, string) The URL for the image location.)
        """
        def set_ImageLocation(self, value):
            InputSet._set_input(self, 'ImageLocation', value)

        """
        Set the value of the ImageType input for this choreography. ((optional, string) The type of image (Main, Alternate, or Swatch). Defaults to "Main".)
        """
        def set_ImageType(self, value):
            InputSet._set_input(self, 'ImageType', value)

        """
        Set the value of the SKU input for this choreography. ((required, string) A SKU is a "Stock Keeping Unit" which you can assign to your products to track your inventory. Provide the SKU for the product that is associated with the image you are uploading.)
        """
        def set_SKU(self, value):
            InputSet._set_input(self, 'SKU', value)

        """
        Set the value of the TimeToWait input for this choreography. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        def set_TimeToWait(self, value):
            InputSet._set_input(self, 'TimeToWait', value)


"""
A ResultSet with methods tailored to the values returned by the AddOrUpdateProductImage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddOrUpdateProductImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon after submitting the feed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ProcessingStatus" output from this choreography execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
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

class AddOrUpdateProductImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddOrUpdateProductImageResultSet(response, path)
