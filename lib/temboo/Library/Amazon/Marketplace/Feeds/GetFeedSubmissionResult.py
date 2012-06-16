
###############################################################################
#
# GetFeedSubmissionResult
# Returns the feed processing report and the Content-MD5 header.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFeedSubmissionResult(Choreography):

    """
    Create a new instance of the GetFeedSubmissionResult Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/GetFeedSubmissionResult')


    def new_input_set(self):
        return GetFeedSubmissionResultInputSet()

    def _make_result_set(self, result, path):
        return GetFeedSubmissionResultResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFeedSubmissionResultChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFeedSubmissionResult
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFeedSubmissionResultInputSet(InputSet):
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
        Set the value of the FeedSubmissionId input for this choreography. ((required, string) A FeedSubmmissionId value.)
        """
        def set_FeedSubmissionId(self, value):
            InputSet._set_input(self, 'FeedSubmissionId', value)


"""
A ResultSet with methods tailored to the values returned by the GetFeedSubmissionResult choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFeedSubmissionResultResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ContentMD5Header" output from this choreography execution. ((string) The Content MD5 header returned from Amazon. This can used to check against an MD5 hash that you generate before submitting the feed to verify that the feed was submitted correctly.)
        """
        def get_ContentMD5Header(self):
            return self._output.get('ContentMD5Header', None)

class GetFeedSubmissionResultChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFeedSubmissionResultResultSet(response, path)
