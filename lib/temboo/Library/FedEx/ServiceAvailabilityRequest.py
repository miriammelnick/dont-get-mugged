
###############################################################################
#
# ServiceAvailabilityRequest
# Retrieves available shipping options and delivery dates for a specified origin and destination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ServiceAvailabilityRequest(Choreography):

    """
    Create a new instance of the ServiceAvailabilityRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedEx/ServiceAvailabilityRequest')


    def new_input_set(self):
        return ServiceAvailabilityRequestInputSet()

    def _make_result_set(self, result, path):
        return ServiceAvailabilityRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ServiceAvailabilityRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ServiceAvailabilityRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ServiceAvailabilityRequestInputSet(InputSet):
        """
        Set the value of the AccountNumber input for this choreography. ((string) Your FedEx Account Number)
        """
        def set_AccountNumber(self, value):
            InputSet._set_input(self, 'AccountNumber', value)

        """
        Set the value of the AuthenticationKey input for this choreography. ((string) The Production Authentication Key provided by FedEx Web Services)
        """
        def set_AuthenticationKey(self, value):
            InputSet._set_input(self, 'AuthenticationKey', value)

        """
        Set the value of the DestinationCountryCode input for this choreography. ((string) The destination country code to use as an input to the service availability request)
        """
        def set_DestinationCountryCode(self, value):
            InputSet._set_input(self, 'DestinationCountryCode', value)

        """
        Set the value of the DestinationPostalCode input for this choreography. ((string) The destination postal code to use as an input to the service availability request)
        """
        def set_DestinationPostalCode(self, value):
            InputSet._set_input(self, 'DestinationPostalCode', value)

        """
        Set the value of the MeterNumber input for this choreography. ((string) The Production Meter Number provided by FedEx Web Services)
        """
        def set_MeterNumber(self, value):
            InputSet._set_input(self, 'MeterNumber', value)

        """
        Set the value of the OriginCountryCode input for this choreography. ((string) The origin country code to use as an input to the service availability request)
        """
        def set_OriginCountryCode(self, value):
            InputSet._set_input(self, 'OriginCountryCode', value)

        """
        Set the value of the Password input for this choreography. ((string) The Production Password provided by FedEx Web Services)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ShipDate input for this choreography. ((date) The date to use for the service availability request (epoch timestamp in milliseconds or formatted like yyyy-MM-dd))
        """
        def set_ShipDate(self, value):
            InputSet._set_input(self, 'ShipDate', value)


"""
A ResultSet with methods tailored to the values returned by the ServiceAvailabilityRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ServiceAvailabilityRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from FedEx)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ServiceAvailabilityRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ServiceAvailabilityRequestResultSet(response, path)
