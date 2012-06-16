
###############################################################################
#
# GetReportList
# Returns a list of reports that were created in the previous 90 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReportList(Choreography):

    """
    Create a new instance of the GetReportList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportList')


    def new_input_set(self):
        return GetReportListInputSet()

    def _make_result_set(self, result, path):
        return GetReportListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReportList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReportListInputSet(InputSet):
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
        Set the value of the Acknowledged input for this choreography. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to "true" to list order reports that have been acknowledged.)
        """
        def set_Acknowledged(self, value):
            InputSet._set_input(self, 'Acknowledged', value)

        """
        Set the value of the AvailableFromDate input for this choreography. ((optional, date) The earliest date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_AvailableFromDate(self, value):
            InputSet._set_input(self, 'AvailableFromDate', value)

        """
        Set the value of the AvailableToDate input for this choreography. ((optional, date) The most recent date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_AvailableToDate(self, value):
            InputSet._set_input(self, 'AvailableToDate', value)

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
        Set the value of the ReportRequestId input for this choreography. ((optional, integer) A ReportRequestId value. If you pass a ReportRequestId value, other query conditions are ignored.)
        """
        def set_ReportRequestId(self, value):
            InputSet._set_input(self, 'ReportRequestId', value)

        """
        Set the value of the ReportType input for this choreography. ((optional, string) A ReportType enumeration value (i.e. GET_ORDERS_DATA_).)
        """
        def set_ReportType(self, value):
            InputSet._set_input(self, 'ReportType', value)


"""
A ResultSet with methods tailored to the values returned by the GetReportList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReportListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ReportId" output from this choreography execution. ((integer) The report id parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        def get_ReportId(self):
            return self._output.get('ReportId', None)

class GetReportListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReportListResultSet(response, path)
