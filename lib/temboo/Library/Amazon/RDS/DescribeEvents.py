
###############################################################################
#
# DescribeEvents
# Returns events related to DB Instances, DB Security Groups, DB Snapshots and DB Parameter Groups for the past 14 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeEvents(Choreography):

    """
    Create a new instance of the DescribeEvents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DescribeEvents')


    def new_input_set(self):
        return DescribeEventsInputSet()

    def _make_result_set(self, result, path):
        return DescribeEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeEventsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeEvents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeEventsInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Duration input for this choreography. ((optional, integer) The number of minutes to retrieve events for. Defaults to 60.)
        """
        def set_Duration(self, value):
            InputSet._set_input(self, 'Duration', value)

        """
        Set the value of the EndTime input for this choreography. ((optional, date) The end of the time interval for which to retrieve events, specified in ISO 8601 format (i.e. 2009-07-08T18:00Z).)
        """
        def set_EndTime(self, value):
            InputSet._set_input(self, 'EndTime', value)

        """
        Set the value of the Marker input for this choreography. ((optional, integer) If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.)
        """
        def set_Marker(self, value):
            InputSet._set_input(self, 'Marker', value)

        """
        Set the value of the MaxRecords input for this choreography. ((optional, integer) The maximum number of records to include in the response. If more records exist, a marker is included in the response so that the remaining results may be retrieved. Defaults to max (100). Min is 20.)
        """
        def set_MaxRecords(self, value):
            InputSet._set_input(self, 'MaxRecords', value)

        """
        Set the value of the SourceIdentifier input for this choreography. ((optional, string) The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.)
        """
        def set_SourceIdentifier(self, value):
            InputSet._set_input(self, 'SourceIdentifier', value)

        """
        Set the value of the SourceType input for this choreography. ((optional, string) The event source to retrieve events for. If no value is specified, all events are returned. Valid values are: db-instance | db-parameter-group | db-security-group | db-snapshot.)
        """
        def set_SourceType(self, value):
            InputSet._set_input(self, 'SourceType', value)

        """
        Set the value of the StartTime input for this choreography. ((optional, date) The beginning of the time interval to retrieve events for, specified in ISO 8601 format (i.e. 2009-07-08T18:00Z))
        """
        def set_StartTime(self, value):
            InputSet._set_input(self, 'StartTime', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeEvents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeEventsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeEventsResultSet(response, path)
