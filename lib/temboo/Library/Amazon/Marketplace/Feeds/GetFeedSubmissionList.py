
###############################################################################
#
# GetFeedSubmissionList
# Returns a list of all feed submissions submitted in the previous 90 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFeedSubmissionList(Choreography):

    """
    Create a new instance of the GetFeedSubmissionList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/GetFeedSubmissionList')


    def new_input_set(self):
        return GetFeedSubmissionListInputSet()

    def _make_result_set(self, result, path):
        return GetFeedSubmissionListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFeedSubmissionListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFeedSubmissionList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFeedSubmissionListInputSet(InputSet):
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
        Set the value of the FeedProcessingStatusList input for this choreography. ((optional, string) A comma separated list of one or more feed processing statuses by which to filter the list of feed submissions.)
        """
        def set_FeedProcessingStatusList(self, value):
            InputSet._set_input(self, 'FeedProcessingStatusList', value)

        """
        Set the value of the FeedSubmissionIdList input for this choreography. ((optional, string) A comma separated list of FeedSubmmissionId values. If you pass in FeedSubmmissionId values in a request, other query conditions are ignored.)
        """
        def set_FeedSubmissionIdList(self, value):
            InputSet._set_input(self, 'FeedSubmissionIdList', value)

        """
        Set the value of the FeedTypeList input for this choreography. ((optional, string) A comma separated list of one or more FeedType enumeration values by which to filter the list of feed submissions.)
        """
        def set_FeedTypeList(self, value):
            InputSet._set_input(self, 'FeedTypeList', value)

        """
        Set the value of the MaxCount input for this choreography. ((optional, integer) A non-negative integer that indicates the maximum number of feed submissions to return in the list. Defaults to 10. Max is 100.)
        """
        def set_MaxCount(self, value):
            InputSet._set_input(self, 'MaxCount', value)

        """
        Set the value of the SubmittedFromDate input for this choreography. ((optional, date) The earliest submission date that you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_SubmittedFromDate(self, value):
            InputSet._set_input(self, 'SubmittedFromDate', value)

        """
        Set the value of the SubmittedToDate input for this choreography. ((optional, date) The latest submission date that you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_SubmittedToDate(self, value):
            InputSet._set_input(self, 'SubmittedToDate', value)


"""
A ResultSet with methods tailored to the values returned by the GetFeedSubmissionList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFeedSubmissionListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "FeedProcessingStatus" output from this choreography execution. ((string) The FeedProcessingStatus parsed from the Amazon response.)
        """
        def get_FeedProcessingStatus(self):
            return self._output.get('FeedProcessingStatus', None)
        """
        Retrieve the value for the "FeedSubmissionId" output from this choreography execution. ((integer) The FeedSubmissionId parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        def get_FeedSubmissionId(self):
            return self._output.get('FeedSubmissionId', None)

class GetFeedSubmissionListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFeedSubmissionListResultSet(response, path)
