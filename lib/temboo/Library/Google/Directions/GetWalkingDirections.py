
###############################################################################
#
# GetWalkingDirections
#  Generate walking directions between two locations, denoted by address or latitude/longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWalkingDirections(Choreography):

    """
    Create a new instance of the GetWalkingDirections Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Directions/GetWalkingDirections')


    def new_input_set(self):
        return GetWalkingDirectionsInputSet()

    def _make_result_set(self, result, path):
        return GetWalkingDirectionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWalkingDirectionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWalkingDirections
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWalkingDirectionsInputSet(InputSet):
        """
        Set the value of the Alternatives input for this choreography. ((optional, string) If set to true, additional routes will be returned.)
        """
        def set_Alternatives(self, value):
            InputSet._set_input(self, 'Alternatives', value)

        """
        Set the value of the Destination input for this choreography. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be generated (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        def set_Destination(self, value):
            InputSet._set_input(self, 'Destination', value)

        """
        Set the value of the Origin input for this choreography. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be computed (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        def set_Origin(self, value):
            InputSet._set_input(self, 'Origin', value)

        """
        Set the value of the Region input for this choreography. ((optional, string) Enter the region code for the directions, specified as a ccTLD two-character value.)
        """
        def set_Region(self, value):
            InputSet._set_input(self, 'Region', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)

        """
        Set the value of the Units input for this choreography. ((optional, string) Specify the units to be used when displaying results.  Options include, metric, or imperial.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)

        """
        Set the value of the Waypoints input for this choreography. ((optional, string) Specify route waypoints, either by address, or latitude/longitude coordinates.)
        """
        def set_Waypoints(self, value):
            InputSet._set_input(self, 'Waypoints', value)


"""
A ResultSet with methods tailored to the values returned by the GetWalkingDirections choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWalkingDirectionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWalkingDirectionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWalkingDirectionsResultSet(response, path)
