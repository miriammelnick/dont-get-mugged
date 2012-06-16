
###############################################################################
#
# RetrieveReport
# Creates a report request of any report type, polls for the status of the report, and downloads the report when it's available.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveReport(Choreography):

    """
    Create a new instance of the RetrieveReport Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/RetrieveReport')


    def new_input_set(self):
        return RetrieveReportInputSet()

    def _make_result_set(self, result, path):
        return RetrieveReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveReportChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveReport
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveReportInputSet(InputSet):
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
        Set the value of the EndDate input for this choreography. ((optional, date) The end of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ReportType input for this choreography. ((optional, string) A ReportType enumeration value. Defaults to _GET_FLAT_FILE_OPEN_LISTINGS_DATA_.)
        """
        def set_ReportType(self, value):
            InputSet._set_input(self, 'ReportType', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, date) The start of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the TimeToWait input for this choreography. ((optional, integer) By default, the Choreo will wait for 5 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        def set_TimeToWait(self, value):
            InputSet._set_input(self, 'TimeToWait', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveReport choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveReportResultSet(ResultSet):
        """
        Retrieve the value for the "Report" output from this choreography execution. (The report contents.)
        """
        def get_Report(self):
            return self._output.get('Report', None)
        """
        Retrieve the value for the "GeneratedReportId" output from this choreography execution. ((integer) The GeneratedReportId parsed from the Amazon response.)
        """
        def get_GeneratedReportId(self):
            return self._output.get('GeneratedReportId', None)
        """
        Retrieve the value for the "ReportProcessingStatus" output from this choreography execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        def get_ReportProcessingStatus(self):
            return self._output.get('ReportProcessingStatus', None)
        """
        Retrieve the value for the "ReportRequestId" output from this choreography execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        def get_ReportRequestId(self):
            return self._output.get('ReportRequestId', None)

class RetrieveReportChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveReportResultSet(response, path)
