<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" maxScale="0" labelsEnabled="1" simplifyDrawingTol="1" simplifyLocal="1" simplifyDrawingHints="0" readOnly="0" simplifyAlgorithm="0" styleCategories="AllStyleCategories" minScale="100000000" version="3.18.0-Zürich" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" startField="" endField="" durationUnit="min" fixedDuration="0" startExpression="" enabled="0" accumulate="0" durationField="" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 enableorderby="0" type="RuleRenderer" forceraster="0" symbollevels="0">
    <rules key="{a35e9511-cd02-4958-a73f-2e78890722de}">
      <rule key="{c1426953-faac-415b-b74e-6368ed4539e1}" symbol="0" label="most advantageous YKR zones (urban center walking and border zones and intensive mass transit)" filter="&quot;zone&quot; = 837101 OR &quot;zone&quot;= 1 OR &quot;zone&quot; = 2 OR &quot;zone&quot;= 3 OR &quot;zone&quot;= 10"/>
      <rule key="{fd14ec04-af59-45a4-b89d-06bb06885320}" symbol="1" label="other zones" filter="ELSE"/>
    </rules>
    <symbols>
      <symbol type="fill" clip_to_extent="1" name="0" force_rhr="0" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" pass="0" enabled="1" class="SimpleFill">
          <Option type="Map">
            <Option type="QString" name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="color" value="255,154,1,255"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="offset" value="0,0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="outline_color" value="252,252,252,255"/>
            <Option type="QString" name="outline_style" value="no"/>
            <Option type="QString" name="outline_width" value="0"/>
            <Option type="QString" name="outline_width_unit" value="MM"/>
            <Option type="QString" name="style" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,154,1,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="252,252,252,255" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" clip_to_extent="1" name="1" force_rhr="0" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" pass="0" enabled="1" class="SimpleFill">
          <Option type="Map">
            <Option type="QString" name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="color" value="2,111,188,255"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="offset" value="0,0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="outline_color" value="252,252,252,255"/>
            <Option type="QString" name="outline_style" value="no"/>
            <Option type="QString" name="outline_width" value="0"/>
            <Option type="QString" name="outline_width_unit" value="MM"/>
            <Option type="QString" name="style" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="2,111,188,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="252,252,252,255" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style capitalization="0" fontKerning="1" fontWeight="50" blendMode="0" fontSize="5" fontItalic="0" allowHtml="0" textOpacity="1" fontStrikeout="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="31,30,29,255" fontUnderline="0" useSubstitutions="0" namedStyle="Normaali" fontSizeUnit="Point" previewBkgrdColor="255,255,255,255" fontWordSpacing="0" isExpression="1" multilineHeight="1" fieldName="yhteensa_tco2" fontLetterSpacing="0" textOrientation="horizontal" fontFamily="MS Shell Dlg 2">
        <text-buffer bufferOpacity="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1" bufferDraw="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1"/>
        <text-mask maskType="0" maskSizeUnits="MM" maskJoinStyle="128" maskSize="0" maskedSymbolLayers="" maskEnabled="0" maskOpacity="1" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <background shapeJoinStyle="64" shapeSizeType="0" shapeOffsetY="0" shapeBlendMode="0" shapeSVGFile="" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeOpacity="1" shapeType="0" shapeBorderWidth="0" shapeRadiiUnit="MM" shapeOffsetX="0" shapeBorderColor="128,128,128,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeSizeUnit="MM" shapeSizeY="0" shapeBorderWidthUnit="MM" shapeRotation="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeRadiiY="0">
          <symbol type="marker" clip_to_extent="1" name="markerSymbol" force_rhr="0" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" pass="0" enabled="1" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" name="angle" value="0"/>
                <Option type="QString" name="color" value="125,139,143,255"/>
                <Option type="QString" name="horizontal_anchor_point" value="1"/>
                <Option type="QString" name="joinstyle" value="bevel"/>
                <Option type="QString" name="name" value="circle"/>
                <Option type="QString" name="offset" value="0,0"/>
                <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="offset_unit" value="MM"/>
                <Option type="QString" name="outline_color" value="35,35,35,255"/>
                <Option type="QString" name="outline_style" value="solid"/>
                <Option type="QString" name="outline_width" value="0"/>
                <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="outline_width_unit" value="MM"/>
                <Option type="QString" name="scale_method" value="diameter"/>
                <Option type="QString" name="size" value="2"/>
                <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
                <Option type="QString" name="size_unit" value="MM"/>
                <Option type="QString" name="vertical_anchor_point" value="1"/>
              </Option>
              <prop v="0" k="angle"/>
              <prop v="125,139,143,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetUnit="MM" shadowBlendMode="6" shadowScale="100" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetDist="1" shadowOpacity="0" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetGlobal="1" shadowUnder="0" shadowRadius="0" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format rightDirectionSymbol=">" reverseDirectionSymbol="0" plussign="0" multilineAlign="0" leftDirectionSymbol="&lt;" wrapChar="" autoWrapLength="3" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" formatNumbers="1" decimals="1" addDirectionSymbol="0"/>
      <placement lineAnchorType="0" xOffset="0" repeatDistance="0" geometryGeneratorType="PointGeometry" placementFlags="10" maxCurvedCharAngleOut="-25" fitInPolygonOnly="0" polygonPlacementFlags="2" quadOffset="4" overrunDistanceUnit="MM" placement="1" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" centroidWhole="1" distMapUnitScale="3x:0,0,0,0,0,0" offsetUnits="MapUnit" lineAnchorPercent="0.5" distUnits="MM" dist="0" rotationAngle="0" repeatDistanceUnits="MM" overrunDistance="0" offsetType="0" priority="10" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" centroidInside="1" geometryGeneratorEnabled="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" yOffset="90" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PolygonGeometry"/>
      <rendering scaleVisibility="1" displayAll="1" fontMaxPixelSize="10000" limitNumLabels="0" labelPerPart="0" upsidedownLabels="0" scaleMax="25000" maxNumLabels="2000" zIndex="0" mergeLines="0" scaleMin="1000" drawLabels="1" minFeatureSize="0" fontLimitPixelSize="0" fontMinPixelSize="3" obstacleFactor="1" obstacle="1" obstacleType="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option name="properties"/>
          <Option type="QString" name="type" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
          <Option type="bool" name="drawToAllParts" value="false"/>
          <Option type="QString" name="enabled" value="0"/>
          <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
          <Option type="QString" name="lineSymbol" value="&lt;symbol type=&quot;line&quot; clip_to_extent=&quot;1&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; alpha=&quot;1&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer locked=&quot;0&quot; pass=&quot;0&quot; enabled=&quot;1&quot; class=&quot;SimpleLine&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;align_dash_pattern&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;capstyle&quot; value=&quot;square&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash&quot; value=&quot;5;2&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;customdash_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;dash_pattern_offset_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;draw_inside_polygon&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;joinstyle&quot; value=&quot;bevel&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_color&quot; value=&quot;60,60,60,255&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_style&quot; value=&quot;solid&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_width&quot; value=&quot;0.3&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;line_width_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;offset_unit&quot; value=&quot;MM&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;ring_filter&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;tweak_dash_pattern_on_corners&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;use_custom_dash&quot; value=&quot;0&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;width_map_unit_scale&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;/Option>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option type="double" name="minLength" value="0"/>
          <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="minLengthUnit" value="MM"/>
          <Option type="double" name="offsetFromAnchor" value="0"/>
          <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
          <Option type="double" name="offsetFromLabel" value="0"/>
          <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions" value="fid"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <LinearlyInterpolatedDiagramRenderer upperHeight="10" lowerWidth="0" upperWidth="10" upperValue="12138.6" attributeLegend="1" lowerHeight="0" diagramType="Pie" classificationAttributeExpression=" &quot;vesi_tco2&quot; + &quot;lammitys_tco2&quot; + &quot;jaahdytys_tco2&quot; + &quot;kiinteistosahko_tco2&quot; + &quot;sahko_kotitaloudet_tco2&quot; + &quot;sahko_palv_tco2&quot; + &quot;sahko_tv_tco2&quot; + &quot;hloliikenne_ap_tco2&quot; + &quot;hloliikenne_tp_tco2&quot; + &quot;tvliikenne_tco2&quot; + &quot;palvliikenne_tco2&quot; + &quot;korjaussaneeraus_tco2&quot; " lowerValue="0">
    <DiagramCategory spacingUnit="MM" minimumSize="3" scaleBasedVisibility="1" spacingUnitScale="3x:0,0,0,0,0,0" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" diagramOrientation="Up" showAxis="0" sizeScale="3x:0,0,0,0,0,0" penWidth="0.1" width="15" lineSizeType="MM" rotationOffset="270" backgroundAlpha="255" spacing="0" height="15" scaleDependency="Area" penAlpha="255" penColor="#ffffff" maxScaleDenominator="50000" direction="1" opacity="1" backgroundColor="#ffffff" minScaleDenominator="1000" enabled="0" barWidth="5">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="Lämmitys" field="lammitys_tco2" color="#ca4d41"/>
      <attribute label="Vesi" field="vesi_tco2" color="#418aca"/>
      <attribute label="Henkilöliikenne, ap" field="hloliikenne_ap_tco2" color="#c551bc"/>
      <attribute label="Sähkö, kotitaloudet" field="sahko_kotitaloudet_tco2" color="#ecff3b"/>
      <attribute label="Palveluliikenne" field="palvliikenne_tco2" color="#745d7c"/>
      <attribute label="Sähkö, palvelut" field="sahko_palv_tco2" color="#decd98"/>
      <attribute label="Liikenne, tv" field="tvliikenne_tco2" color="#661f98"/>
      <attribute label="Sähkö, tv" field="sahko_tv_tco2" color="#bbf7d6"/>
      <attribute label="Kiinteistösähkö" field="kiinteistosahko_tco2" color="#3a2f6c"/>
      <attribute label="Henkilöliikenne, tp" field="hloliikenne_tp_tco2" color="#4dee3b"/>
      <attribute label="Korjaussaneeraus" field="korjaussaneeraus_tco2" color="#d6a4ff"/>
      <attribute label="Jäähdytys" field="jaahdytys_tco2" color="#51c7bc"/>
      <axisSymbol>
        <symbol type="line" clip_to_extent="1" name="" force_rhr="0" alpha="1">
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <layer locked="0" pass="0" enabled="1" class="SimpleLine">
            <Option type="Map">
              <Option type="QString" name="align_dash_pattern" value="0"/>
              <Option type="QString" name="capstyle" value="square"/>
              <Option type="QString" name="customdash" value="5;2"/>
              <Option type="QString" name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="customdash_unit" value="MM"/>
              <Option type="QString" name="dash_pattern_offset" value="0"/>
              <Option type="QString" name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="dash_pattern_offset_unit" value="MM"/>
              <Option type="QString" name="draw_inside_polygon" value="0"/>
              <Option type="QString" name="joinstyle" value="bevel"/>
              <Option type="QString" name="line_color" value="35,35,35,255"/>
              <Option type="QString" name="line_style" value="solid"/>
              <Option type="QString" name="line_width" value="0.26"/>
              <Option type="QString" name="line_width_unit" value="MM"/>
              <Option type="QString" name="offset" value="0"/>
              <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offset_unit" value="MM"/>
              <Option type="QString" name="ring_filter" value="0"/>
              <Option type="QString" name="tweak_dash_pattern_on_corners" value="0"/>
              <Option type="QString" name="use_custom_dash" value="0"/>
              <Option type="QString" name="width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            </Option>
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </LinearlyInterpolatedDiagramRenderer>
  <DiagramLayerSettings zIndex="0" placement="4" obstacle="0" linePlacementFlags="18" showAll="1" priority="10" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" name="allowedGapsBuffer" value="0"/>
        <Option type="bool" name="allowedGapsEnabled" value="false"/>
        <Option type="QString" name="allowedGapsLayer" value=""/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="xyind">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="mun">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="zone">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="year">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="floorspace">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="pop">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="tilat_vesi_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="tilat_lammitys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="tilat_jaahdytys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sahko_kiinteistot_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sahko_kotitaloudet_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sahko_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sahko_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="liikenne_hlo_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="liikenne_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="liikenne_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="rak_korjaussaneeraus_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="rak_purku_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="rak_uudis_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_yhteensa_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_lammonsaato_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_liikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_sahko_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_rakentaminen_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="tp_yht">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="pop_per_popjob_percentage">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_yhteensa_tco2_per_asukas">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_yhteensa_tco2_per_tp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_yhteensa_tco2_per_as_tp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sum_yhteensa_tco2_per_kem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="xyind" name="" index="0"/>
    <alias field="mun" name="" index="1"/>
    <alias field="zone" name="" index="2"/>
    <alias field="year" name="" index="3"/>
    <alias field="floorspace" name="" index="4"/>
    <alias field="pop" name="" index="5"/>
    <alias field="tilat_vesi_tco2" name="" index="6"/>
    <alias field="tilat_lammitys_tco2" name="" index="7"/>
    <alias field="tilat_jaahdytys_tco2" name="" index="8"/>
    <alias field="sahko_kiinteistot_tco2" name="" index="9"/>
    <alias field="sahko_kotitaloudet_tco2" name="" index="10"/>
    <alias field="sahko_palv_tco2" name="" index="11"/>
    <alias field="sahko_tv_tco2" name="" index="12"/>
    <alias field="liikenne_hlo_tco2" name="" index="13"/>
    <alias field="liikenne_tv_tco2" name="" index="14"/>
    <alias field="liikenne_palv_tco2" name="" index="15"/>
    <alias field="rak_korjaussaneeraus_tco2" name="" index="16"/>
    <alias field="rak_purku_tco2" name="" index="17"/>
    <alias field="rak_uudis_tco2" name="" index="18"/>
    <alias field="sum_yhteensa_tco2" name="" index="19"/>
    <alias field="sum_lammonsaato_tco2" name="" index="20"/>
    <alias field="sum_liikenne_tco2" name="" index="21"/>
    <alias field="sum_sahko_tco2" name="" index="22"/>
    <alias field="sum_rakentaminen_tco2" name="" index="23"/>
    <alias field="tp_yht" name="" index="24"/>
    <alias field="pop_per_popjob_percentage" name="" index="25"/>
    <alias field="sum_yhteensa_tco2_per_asukas" name="" index="26"/>
    <alias field="sum_yhteensa_tco2_per_tp" name="" index="27"/>
    <alias field="sum_yhteensa_tco2_per_as_tp" name="" index="28"/>
    <alias field="sum_yhteensa_tco2_per_kem" name="" index="29"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="xyind" expression=""/>
    <default applyOnUpdate="0" field="mun" expression=""/>
    <default applyOnUpdate="0" field="zone" expression=""/>
    <default applyOnUpdate="0" field="year" expression=""/>
    <default applyOnUpdate="0" field="floorspace" expression=""/>
    <default applyOnUpdate="0" field="pop" expression=""/>
    <default applyOnUpdate="0" field="tilat_vesi_tco2" expression=""/>
    <default applyOnUpdate="0" field="tilat_lammitys_tco2" expression=""/>
    <default applyOnUpdate="0" field="tilat_jaahdytys_tco2" expression=""/>
    <default applyOnUpdate="0" field="sahko_kiinteistot_tco2" expression=""/>
    <default applyOnUpdate="0" field="sahko_kotitaloudet_tco2" expression=""/>
    <default applyOnUpdate="0" field="sahko_palv_tco2" expression=""/>
    <default applyOnUpdate="0" field="sahko_tv_tco2" expression=""/>
    <default applyOnUpdate="0" field="liikenne_hlo_tco2" expression=""/>
    <default applyOnUpdate="0" field="liikenne_tv_tco2" expression=""/>
    <default applyOnUpdate="0" field="liikenne_palv_tco2" expression=""/>
    <default applyOnUpdate="0" field="rak_korjaussaneeraus_tco2" expression=""/>
    <default applyOnUpdate="0" field="rak_purku_tco2" expression=""/>
    <default applyOnUpdate="0" field="rak_uudis_tco2" expression=""/>
    <default applyOnUpdate="0" field="sum_yhteensa_tco2" expression=""/>
    <default applyOnUpdate="0" field="sum_lammonsaato_tco2" expression=""/>
    <default applyOnUpdate="0" field="sum_liikenne_tco2" expression=""/>
    <default applyOnUpdate="0" field="sum_sahko_tco2" expression=""/>
    <default applyOnUpdate="0" field="sum_rakentaminen_tco2" expression=""/>
    <default applyOnUpdate="0" field="tp_yht" expression=""/>
    <default applyOnUpdate="0" field="pop_per_popjob_percentage" expression=""/>
    <default applyOnUpdate="0" field="sum_yhteensa_tco2_per_asukas" expression=""/>
    <default applyOnUpdate="0" field="sum_yhteensa_tco2_per_tp" expression=""/>
    <default applyOnUpdate="0" field="sum_yhteensa_tco2_per_as_tp" expression=""/>
    <default applyOnUpdate="0" field="sum_yhteensa_tco2_per_kem" expression=""/>
  </defaults>
  <constraints>
    <constraint field="xyind" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="mun" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="zone" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="year" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="floorspace" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="pop" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="tilat_vesi_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="tilat_lammitys_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="tilat_jaahdytys_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sahko_kiinteistot_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sahko_kotitaloudet_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sahko_palv_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sahko_tv_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="liikenne_hlo_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="liikenne_tv_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="liikenne_palv_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="rak_korjaussaneeraus_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="rak_purku_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="rak_uudis_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_yhteensa_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_lammonsaato_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_liikenne_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_sahko_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_rakentaminen_tco2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="tp_yht" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="pop_per_popjob_percentage" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_yhteensa_tco2_per_asukas" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_yhteensa_tco2_per_tp" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_yhteensa_tco2_per_as_tp" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="sum_yhteensa_tco2_per_kem" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="xyind" desc="" exp=""/>
    <constraint field="mun" desc="" exp=""/>
    <constraint field="zone" desc="" exp=""/>
    <constraint field="year" desc="" exp=""/>
    <constraint field="floorspace" desc="" exp=""/>
    <constraint field="pop" desc="" exp=""/>
    <constraint field="tilat_vesi_tco2" desc="" exp=""/>
    <constraint field="tilat_lammitys_tco2" desc="" exp=""/>
    <constraint field="tilat_jaahdytys_tco2" desc="" exp=""/>
    <constraint field="sahko_kiinteistot_tco2" desc="" exp=""/>
    <constraint field="sahko_kotitaloudet_tco2" desc="" exp=""/>
    <constraint field="sahko_palv_tco2" desc="" exp=""/>
    <constraint field="sahko_tv_tco2" desc="" exp=""/>
    <constraint field="liikenne_hlo_tco2" desc="" exp=""/>
    <constraint field="liikenne_tv_tco2" desc="" exp=""/>
    <constraint field="liikenne_palv_tco2" desc="" exp=""/>
    <constraint field="rak_korjaussaneeraus_tco2" desc="" exp=""/>
    <constraint field="rak_purku_tco2" desc="" exp=""/>
    <constraint field="rak_uudis_tco2" desc="" exp=""/>
    <constraint field="sum_yhteensa_tco2" desc="" exp=""/>
    <constraint field="sum_lammonsaato_tco2" desc="" exp=""/>
    <constraint field="sum_liikenne_tco2" desc="" exp=""/>
    <constraint field="sum_sahko_tco2" desc="" exp=""/>
    <constraint field="sum_rakentaminen_tco2" desc="" exp=""/>
    <constraint field="tp_yht" desc="" exp=""/>
    <constraint field="pop_per_popjob_percentage" desc="" exp=""/>
    <constraint field="sum_yhteensa_tco2_per_asukas" desc="" exp=""/>
    <constraint field="sum_yhteensa_tco2_per_tp" desc="" exp=""/>
    <constraint field="sum_yhteensa_tco2_per_as_tp" desc="" exp=""/>
    <constraint field="sum_yhteensa_tco2_per_kem" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column type="field" name="xyind" hidden="0" width="-1"/>
      <column type="field" name="sahko_kotitaloudet_tco2" hidden="0" width="202"/>
      <column type="field" name="sahko_palv_tco2" hidden="0" width="-1"/>
      <column type="field" name="sahko_tv_tco2" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
      <column type="field" name="tilat_vesi_tco2" hidden="0" width="-1"/>
      <column type="field" name="tilat_lammitys_tco2" hidden="0" width="-1"/>
      <column type="field" name="tilat_jaahdytys_tco2" hidden="0" width="-1"/>
      <column type="field" name="sahko_kiinteistot_tco2" hidden="0" width="-1"/>
      <column type="field" name="liikenne_hlo_tco2" hidden="0" width="-1"/>
      <column type="field" name="liikenne_tv_tco2" hidden="0" width="-1"/>
      <column type="field" name="liikenne_palv_tco2" hidden="0" width="-1"/>
      <column type="field" name="rak_korjaussaneeraus_tco2" hidden="0" width="-1"/>
      <column type="field" name="rak_purku_tco2" hidden="0" width="-1"/>
      <column type="field" name="rak_uudis_tco2" hidden="0" width="-1"/>
      <column type="field" name="sum_yhteensa_tco2" hidden="0" width="-1"/>
      <column type="field" name="sum_lammonsaato_tco2" hidden="0" width="-1"/>
      <column type="field" name="sum_liikenne_tco2" hidden="0" width="-1"/>
      <column type="field" name="sum_sahko_tco2" hidden="0" width="-1"/>
      <column type="field" name="sum_rakentaminen_tco2" hidden="0" width="-1"/>
      <column type="field" name="mun" hidden="0" width="-1"/>
      <column type="field" name="zone" hidden="0" width="-1"/>
      <column type="field" name="year" hidden="0" width="-1"/>
      <column type="field" name="floorspace" hidden="0" width="-1"/>
      <column type="field" name="pop" hidden="0" width="-1"/>
      <column type="field" name="sum_yhteensa_tco2_per_asukas" hidden="0" width="-1"/>
      <column type="field" name="tp_yht" hidden="0" width="-1"/>
      <column type="field" name="sum_yhteensa_tco2_per_tp" hidden="0" width="-1"/>
      <column type="field" name="sum_yhteensa_tco2_per_as_tp" hidden="0" width="-1"/>
      <column type="field" name="sum_yhteensa_tco2_per_kem" hidden="0" width="-1"/>
      <column type="field" name="pop_per_popjob_percentage" hidden="0" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.
Use this function to add extra logic to your forms.
Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="fid" editable="1"/>
    <field name="floorspace" editable="1"/>
    <field name="hloliikenne_ap_tco2" editable="1"/>
    <field name="hloliikenne_tco2" editable="1"/>
    <field name="hloliikenne_tp_tco2" editable="1"/>
    <field name="id" editable="1"/>
    <field name="jaahdytys_tco2" editable="1"/>
    <field name="kiinteistosahko_tco2" editable="1"/>
    <field name="korjaussaneeraus_tco2" editable="1"/>
    <field name="lammitys_tco2" editable="1"/>
    <field name="liikenne_hlo_tco2" editable="1"/>
    <field name="liikenne_palv_tco2" editable="1"/>
    <field name="liikenne_tv_tco2" editable="1"/>
    <field name="liikenne_yht" editable="1"/>
    <field name="mun" editable="1"/>
    <field name="palvliikenne_tco2" editable="1"/>
    <field name="pop" editable="1"/>
    <field name="pop_per_popjob_percentage" editable="1"/>
    <field name="purkaminen_tco2" editable="1"/>
    <field name="rak_korjaussaneeraus_tco2" editable="1"/>
    <field name="rak_purku_tco2" editable="1"/>
    <field name="rak_uudis_tco2" editable="1"/>
    <field name="sahko_kiinteistot_tco2" editable="1"/>
    <field name="sahko_kotitaloudet_tco2" editable="1"/>
    <field name="sahko_palv_tco2" editable="1"/>
    <field name="sahko_tv_tco2" editable="1"/>
    <field name="sahko_yht" editable="1"/>
    <field name="sum_lammonsaato_tco2" editable="1"/>
    <field name="sum_liikenne_tco2" editable="1"/>
    <field name="sum_rakentaminen_tco2" editable="1"/>
    <field name="sum_sahko_tco2" editable="1"/>
    <field name="sum_yhteensa_tco2" editable="1"/>
    <field name="sum_yhteensa_tco2_per_as_tp" editable="1"/>
    <field name="sum_yhteensa_tco2_per_asukas" editable="1"/>
    <field name="sum_yhteensa_tco2_per_kem" editable="1"/>
    <field name="sum_yhteensa_tco2_per_tp" editable="1"/>
    <field name="summa" editable="1"/>
    <field name="tilat_jaahdytys_tco2" editable="1"/>
    <field name="tilat_lammitys_tco2" editable="1"/>
    <field name="tilat_vesi_tco2" editable="1"/>
    <field name="tp_yht" editable="1"/>
    <field name="tvliikenne_tco2" editable="1"/>
    <field name="uudisrakentaminen_tco2" editable="1"/>
    <field name="vesi_tco2" editable="1"/>
    <field name="vuosi" editable="1"/>
    <field name="xyind" editable="1"/>
    <field name="year" editable="1"/>
    <field name="yhteensa_tco2" editable="1"/>
    <field name="zone" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="fid" labelOnTop="0"/>
    <field name="floorspace" labelOnTop="0"/>
    <field name="hloliikenne_ap_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tp_tco2" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="jaahdytys_tco2" labelOnTop="0"/>
    <field name="kiinteistosahko_tco2" labelOnTop="0"/>
    <field name="korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="lammitys_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2" labelOnTop="0"/>
    <field name="liikenne_palv_tco2" labelOnTop="0"/>
    <field name="liikenne_tv_tco2" labelOnTop="0"/>
    <field name="liikenne_yht" labelOnTop="0"/>
    <field name="mun" labelOnTop="0"/>
    <field name="palvliikenne_tco2" labelOnTop="0"/>
    <field name="pop" labelOnTop="0"/>
    <field name="pop_per_popjob_percentage" labelOnTop="0"/>
    <field name="purkaminen_tco2" labelOnTop="0"/>
    <field name="rak_korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="rak_purku_tco2" labelOnTop="0"/>
    <field name="rak_uudis_tco2" labelOnTop="0"/>
    <field name="sahko_kiinteistot_tco2" labelOnTop="0"/>
    <field name="sahko_kotitaloudet_tco2" labelOnTop="0"/>
    <field name="sahko_palv_tco2" labelOnTop="0"/>
    <field name="sahko_tv_tco2" labelOnTop="0"/>
    <field name="sahko_yht" labelOnTop="0"/>
    <field name="sum_lammonsaato_tco2" labelOnTop="0"/>
    <field name="sum_liikenne_tco2" labelOnTop="0"/>
    <field name="sum_rakentaminen_tco2" labelOnTop="0"/>
    <field name="sum_sahko_tco2" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_as_tp" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_asukas" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_kem" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_tp" labelOnTop="0"/>
    <field name="summa" labelOnTop="0"/>
    <field name="tilat_jaahdytys_tco2" labelOnTop="0"/>
    <field name="tilat_lammitys_tco2" labelOnTop="0"/>
    <field name="tilat_vesi_tco2" labelOnTop="0"/>
    <field name="tp_yht" labelOnTop="0"/>
    <field name="tvliikenne_tco2" labelOnTop="0"/>
    <field name="uudisrakentaminen_tco2" labelOnTop="0"/>
    <field name="vesi_tco2" labelOnTop="0"/>
    <field name="vuosi" labelOnTop="0"/>
    <field name="xyind" labelOnTop="0"/>
    <field name="year" labelOnTop="0"/>
    <field name="yhteensa_tco2" labelOnTop="0"/>
    <field name="zone" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
