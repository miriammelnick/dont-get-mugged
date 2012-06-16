
###############################################################################
#
# GetReportRequestList
# Returns a list of report requests that you can use to get the ReportProcessingStatus and ReportId in order to retrieve a report.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReportRequestList(Choreography):

    """
    Create a new instance of the GetReportRequestList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportRequestList')


    def new_input_set(self):
        return GetReportRequestListInputSet()

    def _make_result_set(self, result, path):
        return GetReportRequestListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportRequestListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReportRequestList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReportRequestListInputSet(InputSet):
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
        Set the value of the MaxCount input for this choreography. ((optional, integer) A non-negative integer that represents the maximum number of report requests to return. Defaults to 10. Max is 100.)
        """
        def set_MaxCount(self, value):
            InputSet._set_input(self, 'MaxCount', value)

        """
        Set the value of the ReportProcessingStatusList input for this choreography. ((optional, string) A comma separated list of up to three ReportProcessingStatuses by which to filter report requests.)
        """
        def set_ReportProcessingStatusList(self, value):
            InputSet._set_input(self, 'ReportProcessingStatusList', value)

        """
        Set the value of the ReportRequestIdList input for this choreography. ((optional, string) A comma separated list of up to three ReportRequestId values. If you pass in a ReportRequestId values, other query conditions are ignored.)
        """
        def set_ReportRequestIdList(self, value):
            InputSet._set_input(self, 'ReportRequestIdList', value)

        """
        Set the value of the ReportTypeList input for this choreography. ((optional, string) A comma separated list of up to three ReportType enumeration values.)
        """
        def set_ReportTypeList(self, value):
            InputSet._set_input(self, 'ReportTypeList', value)

        """
        Set the value of the RequestedFromDate input for this choreography. ((optional, date) The start of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_RequestedFromDate(self, value):
            InputSet._set_input(self, 'RequestedFromDate', value)

        """
        Set the value of the RequestedToDate input for this choreography. ((optional, date) The end of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_RequestedToDate(self, value):
            InputSet._set_input(self, 'RequestedToDate', value)


"""
A ResultSet with methods tailored to the values returned by the GetReportRequestList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReportRequestListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "GeneratedReportId" output from this choreography execution. ((integer) The GeneratedReportId parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        def get_GeneratedReportId(self):
            return self._output.get('GeneratedReportId', None)
        """
        Retrieve the value for the "ReportProcessingStatus" output from this choreography execution. ((string) The report status parsed from the Amazon response. If multiple records are returned, this output variable will contain the report status in the list.)
        """
        def get_ReportProcessingStatus(self):
            return self._output.get('ReportProcessingStatus', None)
        """
        Retrieve the value for the "ReportRequestId" output from this choreography execution. ((integer) The report request id parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        def get_ReportRequestId(self):
            return self._output.get('ReportRequestId', None)

class GetReportRequestListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReportRequestListResultSet(response, path)
