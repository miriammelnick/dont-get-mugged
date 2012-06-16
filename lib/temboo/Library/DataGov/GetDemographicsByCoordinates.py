
###############################################################################
#
# GetDemographicsByCoordinates
# Retrieve demographic information for specified geographical coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDemographicsByCoordinates(Choreography):

    """
    Create a new instance of the GetDemographicsByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsByCoordinates')


    def new_input_set(self):
        return GetDemographicsByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDemographicsByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDemographicsByCoordinatesInputSet(InputSet):
        """
        Set the value of the DataVersion input for this choreography. ((optional, string) Specify the data version to search, such as "jun2011" (the default).)
        """
        def set_DataVersion(self, value):
            InputSet._set_input(self, 'DataVersion', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) Specify a latitude to search for, such as "41.486857".)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) Specify a longitude to search for, such as "-71.294392".)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the GetDemographicsByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDemographicsByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from the API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDemographicsByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsByCoordinatesResultSet(response, path)
